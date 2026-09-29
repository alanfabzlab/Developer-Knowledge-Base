#!/usr/bin/env python3
"""
check_notes.py — coherencia interna de las notas, en todo el vault.

Detecta lo que un lector nota tarde y git nunca señala:

  FENCES      un ``` sin pareja, o una etiqueta de lenguaje inventada. Un
              fence desbalanceado se come el resto de la nota al renderizar.
  TABLAS      una fila con más o menos columnas que la cabecera. Rompe el
              ancho de la tabla y hides el contenido que sobra.
  WIKILINKS   un [[Enlace]] que no apunta a ningún archivo. Obsidian lo deja
              como texto plano, así que el enlace roto es invisible.
  ALERTAS     un `> [!X]` con un tipo que GitHub no reconoce, o con texto
              detrás del marcador. GitHub solo entiende NOTE, TIP, IMPORTANT,
              WARNING y CAUTION, y solo si el marcador va solo en su línea;
              cualquier otra cosa se dibuja como una cita normal con los
              corchetes a la vista.

Los wikilinks se resuelven contra todo el vault, no contra el módulo, porque
Obsidian también resuelve entre módulos.

Uso:  python3 tools/check_notes.py [raíz]     (por defecto, la raíz del repo)
Salida: 0 si todo cuadra; 1 si hay algún problema.
"""
import os
import re
import sys

FENCE = re.compile(r'^```(\S*)')
TABLE_DELIM = re.compile(r'^\|[\s:\-|]+\|$')
WIKILINK = re.compile(r'\[\[([^\]]+)\]\]')
# The five alert types GitHub renders as coloured boxes.
GITHUB_ALERTS = {'NOTE', 'TIP', 'IMPORTANT', 'WARNING', 'CAUTION'}
KNOWN_TAGS = {'bash', 'sh', 'shell', 'text', 'txt', 'mermaid', 'json',
              'yaml', 'toml', 'python', 'csharp', 'cs', 'cpp', 'c', 'java',
              'html', 'css', 'js', 'javascript', 'typescript', 'sql', 'diff',
              'gitignore', 'tree', 'env', ''}
SKIP_DIRS = {'z_attachments', 'copilot', '.opencode', '.copilot', 'tools',
             'node_modules', '__pycache__', '.git'}


def columns(row):
    """Column count, ignoring pipes that are content rather than separators.

    A pipe inside backticks is part of a value, not a break, and so is one the
    author escaped as `\\|`. Both appear in these notes (the C# operator table
    documents `||`), and counting them turns a correct row into a false alarm.
    """
    masked = re.sub(r'`[^`]*`', 'C', row)
    return len(re.findall(r'(?<!\\)\|', masked)) - 1



def module_dirs(root):
    """Directorios de primer nivel que contienen notas, en orden."""
    return [d for d in sorted(os.listdir(root))
            if os.path.isdir(os.path.join(root, d))
            and d not in SKIP_DIRS and not d.startswith('.')
            and any(f.endswith('.md') for f in os.listdir(os.path.join(root, d)))]


def build_index(root):
    """Nombres resolubles por un wikilink: nombre completo y su cola.

    Obsidian permite `[[CSharp]]` para un archivo titulado `... CSharp.md`, y
    en la práctica es como se enlazan los proyectos de los distintos módulos.
    """
    stems, tails = set(), set()
    for d in ['.'] + module_dirs(root):
        for f in sorted(os.listdir(os.path.join(root, d))):
            if f.endswith('.md'):
                stems.add(f[:-3])
                tails.add(f.split(' - ')[-1][:-3])
    return stems, tails


def check(path, name, rel, index):
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')
    problems = []

    # --- fences ---
    fences = [i for i, l in enumerate(lines, 1) if l.startswith('```')]
    if len(fences) % 2:
        problems.append(f'{rel}:{fences[-1]}: ``` sin cerrar '
                        f'({len(fences)} en total)')
    for i, l in enumerate(lines, 1):
        m = FENCE.match(l)
        if m and m.group(1).lower() not in KNOWN_TAGS:
            problems.append(f'{rel}:{i}: etiqueta de fence desconocida '
                            f'```{m.group(1)}')

    # --- tables: a header is a `|` row immediately followed by a delimiter,
    #     and every row after it must have the header's column count ---
    header = None
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith('|') and s.endswith('|'):
            cols = columns(s)
            nxt = lines[i].strip() if i < len(lines) else ''
            if TABLE_DELIM.match(s):
                if header is None:
                    problems.append(f'{rel}:{i}: separador de tabla sin cabecera')
                elif cols != header:
                    problems.append(f'{rel}:{i}: separador con {cols} columnas, '
                                    f'la cabecera tiene {header}')
            elif TABLE_DELIM.match(nxt):
                header = cols
            elif header is None:
                problems.append(f'{rel}:{i}: fila de tabla sin cabecera previa')
            elif cols != header:
                problems.append(f'{rel}:{i}: {cols} columnas, la cabecera tiene '
                                f'{header}')
        else:
            header = None

    # --- wikilinks ---
    stems, tails = index
    for m in WIKILINK.finditer(text):
        target = m.group(1).split('|')[0].split('#')[0].strip()
        if not target or target.startswith(('http', '<')):
            continue
        stem = target[:-3] if target.endswith('.md') else target
        if stem not in stems and stem not in tails:
            problems.append(f'{rel}: wikilink roto -> [[{m.group(1)}]]')

    # --- alerts ---
    for i, l in enumerate(lines, 1):
        m = re.match(r'^>\s*\[!(\w+)\](.*)$', l)
        if m:
            kind, rest = m.group(1).upper(), m.group(2).strip()
            if kind not in GITHUB_ALERTS:
                problems.append(f'{rel}:{i}: alerta [!{m.group(1)}] no la '
                                f'reconoce GitHub (use NOTE, TIP, IMPORTANT, '
                                f'WARNING o CAUTION)')
            if rest:
                problems.append(f'{rel}:{i}: el marcador [!{m.group(1)}] debe '
                                f'ir solo en su linea, no seguido de {rest!r}')
    return problems


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                           else os.path.dirname(os.path.dirname(
                               os.path.abspath(__file__))))
    index = build_index(root)
    problems, checked = [], 0

    for d in ['.'] + module_dirs(root):
        base = os.path.join(root, d)
        for f in sorted(os.listdir(base)):
            if f.endswith('.md'):
                checked += 1
                rel = os.path.relpath(os.path.join(base, f), root)
                problems += check(os.path.join(base, f), f, rel, index)

    print(f'notas revisadas: {checked}')
    if problems:
        print(f'\n=== PROBLEMAS ({len(problems)}) ===')
        for p in problems:
            print(f'  {p}')
        return 1
    print('RESULTADO: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
