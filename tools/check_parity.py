#!/usr/bin/env python3
"""
check_parity.py — que el espejo español exista y vaya al mismo paso.

El vault promete que toda nota existe en ambos idiomas, y que la versión
española es un espejo de la inglesa. Esa promesa se rompe en silencio: se
añade una nota nueva y no se traduce, o se traduce pero se le olvida un
bloque de código, y nadie se entera hasta que un lector llega a un `##` sin
contenido.

Empareja por prefijo numérico dentro de cada módulo (`01` inglés con `01`
español), que es como el vault ordena las notas. Los README y las chuletas se
comprueban aparte, porque no llevan prefijo.

Compara, nota a nota:

  * que exista la pareja en los dos idiomas;
  * el mismo número de bloques ```bash;
  * los mismos comandos uno a uno, en el mismo orden. Las metavariables se
    normalizan a un token, porque traducir `<source>` como `<origen>` es
    traducir la sintaxis, no cambiar el ejemplo. Cualquier otra diferencia sí
    es un defecto: si el inglés hace `mv` y el español hace `cp`, el lector
    avanza por dos lecciones distintas.

Lo que NO se comprueba aquí, y conviene saberlo: el texto corrido. Que dos
notas traducibles no compartan literalmente ninguna frase es normal y sano;
forzarlo produciría traducciones robóticas.

Uso:  python3 tools/check_parity.py [raíz]     (por defecto, la raíz del repo)
Salida: 0 si todo cuadra; 1 si alguna nota está descuadrada.
"""
import os
import re
import sys

BASH_BLOCK = re.compile(r'^```bash\n(.*?)^```', re.M | re.S)
PLACEHOLDER = re.compile(r'<[^<>]+>')
SKIP_DIRS = {'z_attachments', 'copilot', '.opencode', '.copilot', 'tools',
             'node_modules', '__pycache__', '.git'}


def is_spanish(text):
    return 'Versión original en inglés' in text


def number_of(name):
    m = re.match(r'^(\d+)', name)
    return m.group(1) if m else None


def commands(block):
    return [l[2:].strip() for l in block.split('\n') if l.startswith('$ ')]


def shape(cmd):
    """A command reduced to its structure: placeholders become one token."""
    return re.sub(r'\s+', ' ', PLACEHOLDER.sub('X', cmd)).strip()


def read(path):
    return open(path, encoding='utf-8').read()


def pair_module(base, rel, problems):
    """-> (pairs, unpaired) for one module directory."""
    en, es, unpaired = {}, {}, []
    for f in sorted(os.listdir(base)):
        if not f.endswith('.md'):
            continue
        num = number_of(f)
        if num is None:
            # MOC and cheatsheets without a number: matched by stem below
            continue
        text = read(os.path.join(base, f))
        (es if is_spanish(text) else en)[num] = (f, text)

    for num in sorted(set(en) | set(es)):
        if num not in en:
            problems.append(f'{rel}/{es[num][0]}: sin original en ingles')
        elif num not in es:
            problems.append(f'{rel}/{en[num][0]}: sin traduccion al espanol')
        else:
            en_name, en_text = en[num]
            es_name, es_text = es[num]
            eb = BASH_BLOCK.findall(en_text)
            sb = BASH_BLOCK.findall(es_text)
            if len(eb) != len(sb):
                problems.append(f'{rel}/{en_name}: {len(eb)} bloques bash EN '
                                f'vs {len(sb)} en {es_name}')
                continue
            for i, (a, b) in enumerate(zip(eb, sb), 1):
                ca, cb = commands(a), commands(b)
                if len(ca) != len(cb):
                    problems.append(f'{rel}/{en_name} bloque {i}: {len(ca)} '
                                    f'comandos EN vs {len(cb)} en {es_name}')
                    continue
                for j, (x, y) in enumerate(zip(ca, cb), 1):
                    if shape(x) != shape(y):
                        problems.append(
                            f'{rel}/{en_name} bloque {i} comando {j}:\n'
                            f'      EN: {x}\n      ES: {y}')
    for num, (f, _) in es.items():
        if num not in en:
            unpaired.append(f)
    return len(set(en) & set(es)), unpaired


def pair_docs(base, rel, problems):
    """MOC pairs: README.md <-> README-ES.md, cheatsheets by stem."""
    files = [f for f in sorted(os.listdir(base)) if f.endswith('.md')]
    es_docs = {f for f in files if f.endswith('-ES.md')}
    for f in es_docs:
        en_name = f[:-len('-ES.md')] + '.md'
        if en_name not in files:
            problems.append(f'{rel}/{f}: sin original {en_name}')
    return len(es_docs)


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                           else os.path.dirname(os.path.dirname(
                               os.path.abspath(__file__))))
    problems = []
    total_pairs = total_docs = 0

    print(f'{"modulo":<36}{"notas EN/ES":>14}{"documentos ES":>16}')
    for d in sorted(os.listdir(root)):
        base = os.path.join(root, d)
        if not os.path.isdir(base) or d in SKIP_DIRS or d.startswith('.'):
            continue
        if not any(f.endswith('.md') for f in os.listdir(base)):
            continue
        pairs, _ = pair_module(base, d, problems)
        docs = pair_docs(base, d, problems)
        total_pairs += pairs
        total_docs += docs
        print(f'{d[:35]:<36}{pairs:>14}{docs:>16}')

    print(f'\npares de notas EN/ES: {total_pairs}')
    print(f'documentos con espejo: {total_docs}')
    if problems:
        print(f'\n=== DESAJUSTES ({len(problems)}) ===')
        for p in problems:
            print(f'  {p}')
        return 1
    print('RESULTADO: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
