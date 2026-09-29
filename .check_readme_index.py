#!/usr/bin/env python3
"""
check_readme_index.py — anti-drift para los README del vault.

Detecta los dos fallos que aparecen solos con el tiempo:

  HUÉRFANAS  una nota .md en disco que ningún README enlaza (típico:
             creas la nota y olvidas meterla en el índice del módulo).
  ENLACES     destinos que no existen, y percent-encoding que no es
             UTF-8 válido de exactamente 2 dígitos hex por byte
             (%C3%Asqueda falla, %C3%BAsqueda pasa).

También informa de notas enlazadas en un solo idioma: es información,
no fallo — una nota de un solo idioma es EN-only por diseño.

Uso:  python3 check_readme_index.py [raíz]     (por defecto, cwd)
Salida: 0 si todo cuadra; 1 si hay huérfanas o enlaces rotos.
"""
import os
import re
import sys
import urllib.parse

LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)\)')
HEX = set('0123456789abcdefABCDEF')
SKIP_DIRS = {'z_attachments', 'copilot', '.opencode', '.copilot',
             'node_modules', '__pycache__'}
README_NAMES = ('README.md', 'README-ES.md')


def norm(p):
    return os.path.normpath(os.path.abspath(p))


def check_encoding(url, where, bad):
    """Exige %XX con exactamente dos dígitos hex, byte a byte."""
    i = 0
    while i < len(url):
        if url[i] == '%':
            chunk = url[i + 1:i + 3]
            if len(chunk) < 2 or any(c not in HEX for c in chunk):
                bad.append(f'{where}: percent-encoding malformado en {url!r}')
                return
            i += 3
        else:
            i += 1


def walk_md(root):
    """Todos los .md del vault, saltando carpetas de tooling y ocultas."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in SKIP_DIRS and not d.startswith('.'))
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                yield os.path.join(dirpath, fn)


def scan(readme, bad):
    """Ficheros .md enlazados desde un README, como rutas absolutas."""
    base = os.path.dirname(readme)
    here = os.path.relpath(readme)
    linked = set()
    for m in LINK.finditer(open(readme, encoding='utf-8').read()):
        url = m.group(2)
        if url.startswith(('http://', 'https://', 'mailto:')) or url.startswith('#'):
            continue
        check_encoding(url, here, bad)
        target = urllib.parse.unquote(url.split('#')[0]).split('?')[0]
        if not target:
            continue
        full = norm(os.path.join(base, target))
        if os.path.isdir(full):
            continue
        if not os.path.isfile(full):
            bad.append(f'{here}: enlace roto -> {url}')
            continue
        if full.endswith('.md'):
            linked.add(full)
    return linked


def main():
    root = norm(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
    bad, orphans, unpaired = [], [], []

    all_md = list(walk_md(root))
    readmes = [p for p in all_md if os.path.basename(p) in README_NAMES]
    linked_anywhere = set()
    by_dir = {}

    for rm in readmes:
        found = scan(rm, bad)
        by_dir[rm] = found
        linked_anywhere |= found

    # 1. Huérfanas: notas de contenido que ningún README enlaza
    for p in all_md:
        if os.path.basename(p) in README_NAMES or norm(p) in linked_anywhere:
            continue
        if os.path.getsize(p) == 0:
            unpaired.append((p, 'nota vacía, enlazada en un solo idioma'))
        else:
            orphans.append(p)

    # 2. Recuento por módulo. En un vault monolingüe cada nota se enlaza
    #    desde un solo idioma, así que lo útil es comparar los totales
    #    EN vs ES: una diferencia señala una nota sin traducir (o al revés).
    print('\nMódulo                              EN  ES  nota')
    mods = sorted({os.path.dirname(p) for p in readmes
                   if os.path.basename(p) == 'README.md'})
    for d in mods:
        en_p = norm(os.path.join(d, 'README.md'))
        es_p = norm(os.path.join(d, 'README-ES.md'))
        on_disk = [os.path.basename(p) for p in all_md
                   if os.path.dirname(norm(p)) == d
                   and os.path.basename(p) not in README_NAMES]
        n_en = len(by_dir.get(en_p, set()))
        n_es = len(by_dir.get(es_p, set()))
        notes = [f'{b} (vacía)' for b in on_disk
                 if os.path.getsize(norm(os.path.join(d, b))) == 0]
        if n_en != n_es:
            notes.append('descuadre EN/ES')
        label = os.path.basename(d) if os.path.basename(d) else '(raíz)'
        print(f'{label[:33]:<34}{n_en:>3}{n_es:>4}  {", ".join(notes) or "-"}')

    print(f'READMEs: {len(readmes)}  '
          f'| .md enlazados: {len(linked_anywhere)}  '
          f'| .md en disco: {len(all_md)}')

    if orphans:
        print('\n=== NOTAS HUÉRFANAS ===')
        for p in orphans:
            print(f'  {os.path.relpath(p, root)}: no enlazada desde ningún README')

    if bad:
        print('\n=== ERRORES ===')
        for b in bad:
            print(f'  {b}')

    if bad or orphans:
        print('\nRESULTADO: FALLA')
        return 1
    print('RESULTADO: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
