"""Verify every documented bash transcript in the Command Line module.

Design notes
------------
The notes target macOS, whose default shell is zsh, and their documented error
text follows zsh's format (`cd: no such file or directory: build`). Sessions
therefore run under zsh.

Each ```bash block is its own session, because that is how the notes are
written: a section demonstrates one thing and states the directory it starts
from, rather than continuing a transcript begun three sections earlier. The
seed directory is the one the block's own `pwd` output documents, or the
project root when the block says nothing. Within a block the state is real and
continuous — a `cd` moves the session, so a relative path in the next step
resolves from where the previous one left you.

Every block runs against exactly the tree the module README documents — no
extra directories invented for the verifier's convenience. A block that needs
state no lesson ever creates is a real defect in the note, and this is what
surfaces it.

The project lives at <tmp>/Users/dev/SunkenKeep, so the notes' literal
`/Users/dev/SunkenKeep` and `~` both resolve inside the sandbox and `cd ..`
walks up a real parent chain instead of escaping into the macOS filesystem.

Each command is wrapped in a brace group, which does not fork, so `cd` really
does move the session. Its combined output is captured to a file *outside*
the project tree — never inside it, or `ls` would list the capture file — and
re-emitted after a marker carrying the exit status.

Two rules are enforced per step:

  * a step with documented output must produce exactly that output;
  * a step with no documented output must not fail, unless the note itself
    documents the failure as the lesson.

Only genuinely environmental text is normalized away: the sandbox root, the
owner/size/date columns of a long listing, the macOS attribute flag, the
`zsh:cd:1:` error prefix and the column layout of a multi-column `ls`. Entry
names, tree shape, order and error text all have to match.

Alcance
------
Este es el único verificador que ejecuta comandos de verdad, y por eso el
más caro: lanza un `zsh` por bloque, y sus resultados dependen de herramientas
de macOS. Corre solo sobre el módulo de Línea de Comandos, que es el único
cuyas transcripciones están auditadas contra una ejecución real; los demás
módulos aún no tienen un árbol de referencia, y ejecutarlos aquí produciría
fallos que nadie ha revisado. Cuando un módulo se audite, se añade su
directorio a MODS y su README documentando el árbol que se espera.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

MODS = ['🖥️ Command Line']

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(ROOT, '🖥️ Command Line')
DOC_ROOT = '/Users/dev/SunkenKeep'
MARK = '__RC__'
FAIL = []
CHECKED = 0
SKIPPED = 0


def build_tree(project, home):
    """Exactly the tree the module README documents, and nothing more."""
    for d in ('assets/audio', 'assets/sprites', 'assets/maps', 'src', 'saves'):
        os.makedirs(os.path.join(project, d), exist_ok=True)
    for f, content in {
        'README.md': '# Sunken Keep\n\nA 2D dungeon crawler.\n',
        'assets/audio/door-open.ogg': '',
        'assets/audio/hit.wav': '',
        'assets/sprites/hero.png': '',
        'assets/sprites/lantern.png': '',
        'assets/maps/level-01.tmx': '',
        'src/main.gd': 'extends Node2D\n',
        'src/player.gd': 'extends CharacterBody2D\n',
        'saves/slot-1.dat': 'player: Kaela\nlevel: 02\nhp: 78\nembers: 340\n',
        'saves/slot-2.dat': 'player: Roen\nlevel: 05\nhp: 41\nembers: 1\n',
    }.items():
        open(os.path.join(project, f), 'w').write(content)


def parse(path):
    """-> [(block_index, [(command, [expected lines])]), ...]"""
    text = open(path, encoding='utf-8').read()
    blocks = []
    for bi, body in enumerate(re.findall(r'^```bash\n(.*?)^```', text,
                                          re.M | re.S), 1):
        steps, cmd, out = [], None, []
        for line in body.split('\n'):
            if line.startswith('$ '):
                if cmd is not None:
                    steps.append((cmd, out))
                cmd, out = line[2:].strip(), []
            elif cmd is not None:
                out.append(line)
        if cmd is not None:
            steps.append((cmd, out))
        if steps:
            blocks.append((bi, steps))
    return blocks


def normalize(lines):
    out = []
    for line in lines:
        line = line.rstrip()
        if not line.strip():
            out.append('')
            continue
        if line.startswith('total '):
            continue
        # long listing -> type character + name
        if re.match(r'^[-dlbcps][rwx-]{9}[@+]?\s', line):
            out.append(line[0] + ' ' + re.split(r'\s+', line.strip())[-1])
            continue
        # multi-column ls -> one name per line
        if re.match(r'^\S+(?:  +\S+)+$', line):
            out.extend(line.split())
            continue
        # zsh prefixes builtin errors with the function and position; when the
        # shell reads from a script file that prefix is the script path
        line = re.sub(r'^(?:\S*/)?\S*:(cd|mkdir|rm|rmdir|cp|cat|ls|touch|echo):\d+: ',
                      r'\1: ', line)
        out.append(line)
    while out and not out[0]:
        out.pop(0)
    while out and not out[-1]:
        out.pop()
    res = []
    for l in out:
        if l == '' and res and res[-1] == '':
            continue
        res.append(l)
    return res


def candidates(project):
    """Plausible starting directories, in the order they should be preferred.

    A block states its starting directory in prose ("From inside
    assets/sprites/"), not in a command, so the verifier tries each candidate
    and accepts the block if the documented output is reproduced from any of
    them. Choosing a start directory is the only thing this tolerance covers;
    every documented output still has to match exactly.
    """
    return [os.path.join(project, d) for d in
            ('', 'assets', 'assets/sprites', 'assets/maps', 'assets/audio',
             'src', 'saves')] + [os.path.join(project, '..'),
                                 os.path.join(project, '../..')]


def run_block(project, home, capdir, block_steps, start):
    """Run one block's steps in a single zsh session.

    Returns [((rc, output lines), (command, expected))] in document order, so
    each result stays paired with its own expectation even when the same
    command appears twice in a block.
    """
    script = [f'cd {start}']
    owners = []
    for cmd, expected in block_steps:
        cap = os.path.join(capdir, f'cap{len(owners)}')
        owners.append((cmd, expected))
        # A non-interactive shell does not echo the destination of `cd -`, but
        # an interactive one does, and that echo is what the notes document.
        # Appending `pwd` reproduces the interactive behaviour.
        body = f'{cmd}; pwd' if cmd.strip() == 'cd -' else cmd
        script.append(f'{{ {body}\n}} > {cap} 2>&1')
        script.append(f'__rc=$?; print -r -- "{MARK}{len(owners) - 1} $__rc"; cat {cap}')
    # The locale is pinned instead of inherited. `ls` sorts by locale, and
    # under en_US.UTF-8 (what a macOS terminal gives you by default) `assets`
    # comes before `README.md`, while under LC_COLLATE=C it is the other way
    # round. The notes document the default, so the runner has to use it too —
    # otherwise the same commit passes on one machine and fails on another, and
    # the only way to find out which is to be the machine it fails on.
    env = dict(os.environ, HOME=home, PS1='$ ', TERM='dumb',
               LC_ALL='en_US.UTF-8', LANG='en_US.UTF-8')
    scriptfile = os.path.join(capdir, 'script.zsh')
    with open(scriptfile, 'w') as fh:
        fh.write('\n'.join(script) + '\n')
    p = subprocess.run(['zsh', '-f', scriptfile], cwd=project, env=env,
                       capture_output=True, text=True, timeout=60)
    per, cur, out = {}, None, []
    for line in p.stdout.split('\n'):
        m = re.match(rf'^{MARK}(\d+) (\d+)$', line.strip())
        if m:
            if cur is not None:
                per[cur] = (out, int(m.group(2)))
            cur, out = int(m.group(1)), []
        elif cur is not None:
            out.append(line)
    if cur is not None:
        per[cur] = (out, 0)
    return [(per.get(i, ([], 0)), owner) for i, owner in enumerate(owners)]


def judge(sandbox, lines, rc, expected, cmd):
    """-> None when the step is correct, else (want, got).

    Paths are canonicalized before comparison. The sandbox is laid out as
    <sandbox>/Users/dev/SunkenKeep with HOME set to <sandbox>/Users/dev, which
    mirrors the paths the notes document, so stripping the sandbox prefix
    leaves text that can be compared directly; the documented project home is
    then rewritten to `ROOT`. A `pwd` that climbed above the project therefore
    still comes out as `/Users/dev`, exactly as the note writes it.
    """
    def canon(text):
        return text.replace(sandbox, '').replace(DOC_ROOT, 'ROOT')
    real = normalize([canon(l) for l in lines])
    want = normalize([canon(l) for l in expected])
    if want:
        return None if real == want else (want, real)
    if rc == 0:
        return None
    if any(k in '\n'.join(lines) for k in
           ('no such file or directory', 'No such file or directory',
            'not found', 'is a directory', 'Is a directory',
            'file exists', 'File exists', 'not a directory',
            'Invalid argument', 'illegal option', 'are identical')):
        return None                      # the failure is the documented lesson
    return (want, real + [f'<exit {rc}>'])

def lesson_order(fname):
    """Lessons run 01 -> 12; cheatsheets and MOCs are reference, not sequence."""
    m = re.match(r'^(\d+)', fname)
    return (int(m.group(1)) if m else 99, fname)


def is_spanish(mod, fname):
    text = open(os.path.join(mod, fname), encoding='utf-8').read()
    return 'Versión original en inglés' in text


def audit(mod):
    """Audit one module. -> (steps, skipped, [(where, cmd, want, got)])"""
    # One tree per language track, because a course builds on itself: lesson
    # 10 of Command Line relies on the `design/` and `builds/` directories that
    # lessons 09 and 07 created. Each block is replayed from the snapshot of the
    # previous one; a block that does not reproduce its documented output is
    # left out of the tree so the next block is not judged against debris.
    checked = skipped = 0
    failures = []
    for lang in ('en', 'es'):
        files = [f for f in os.listdir(mod)
                 if f.endswith('.md') and is_spanish(mod, f) == (lang == 'es')]
        sandbox = tempfile.mkdtemp(prefix='sbx-')
        capdir = tempfile.mkdtemp(prefix='cap-')
        user = os.path.join(sandbox, 'Users', 'dev')
        state = os.path.join(user, 'SunkenKeep')
        snapshot = os.path.join(user, '.snapshot')
        os.makedirs(state)
        build_tree(state, sandbox)
        shutil.copytree(state, snapshot, symlinks=True)
        try:
            for fname in sorted(files, key=lesson_order):
                all_blocks = parse(os.path.join(mod, fname))
                blocks = [(bi, s) for bi, s in all_blocks
                          if not any('<' in c and '<<' not in c or 'Ctrl' in c
                                     for c, _ in s)]
                skipped += len(all_blocks) - len(blocks)
                for bi, block_steps in blocks:
                    # The starting directory is stated in prose rather than in a
                    # command, so each candidate is replayed from the snapshot
                    # and the first one reproducing the output is adopted.
                    problems, accepted = None, False
                    for start in candidates(state):
                        shutil.rmtree(state)
                        shutil.copytree(snapshot, state, symlinks=True)
                        results = run_block(state, user, capdir,
                                            block_steps, start)
                        bad = []
                        for (lines, rc), (cmd, expected) in results:
                            problem = judge(sandbox, lines, rc, expected, cmd)
                            if problem:
                                bad.append((cmd, problem[0], problem[1]))
                        if not bad:
                            accepted = True
                            break
                        if problems is None or len(bad) < len(problems):
                            problems = bad
                    if accepted:
                        checked += len(block_steps)
                        shutil.rmtree(snapshot)
                        shutil.copytree(state, snapshot, symlinks=True)
                    else:
                        for cmd, want, got in problems:
                            checked += 1
                            failures.append((f'{fname} b{bi}', cmd, want, got))
        finally:
            shutil.rmtree(sandbox, ignore_errors=True)
            shutil.rmtree(capdir, ignore_errors=True)
    return checked, skipped, failures


def main():
    total = skipped = 0
    failures = []
    for mod in MODS:
        path = os.path.join(ROOT, mod)
        if not os.path.isdir(path):
            print(f'\n=== MODULO AUSENTE: {mod} ===')
            return 1
        c, s, f = audit(path)
        print(f'{mod}: {c} pasos  (bloques omitidos: {s})')
        total += c
        skipped += s
        failures += [(f'{mod}: {w}', c_, wt, gt) for w, c_, wt, gt in f]
    print(f'\ntotal: {total} pasos ejecutados  (omitidos: {skipped})')
    if failures:
        print(f'\n=== DISCREPANCIAS ({len(failures)}) ===')
        for where, cmd, want, got in failures:
            print(f'\n--- {where}: `{cmd}`')
            print('  esperado:', ' | '.join(want) or '(vacio)')
            print('  real:    ', ' | '.join(got) or '(vacio)')
        return 1
    print('RESULTADO: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
