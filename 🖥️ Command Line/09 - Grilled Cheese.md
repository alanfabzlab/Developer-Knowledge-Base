
# 09. Grilled Cheese

**Spanish version:** [09 - Queso a la Plancha.md](09%20-%20Queso%20a%20la%20Plancha.md)

**Course:** Command Line
**Topic:** Output Redirection, Overwriting vs. Appending, Combining with `cat`
**Tags:** `#cli` `#redirection` `#echo` `#streams` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

So far the shell has only *read* files. Redirection turns it around: instead of printing to the screen, a command's output is written into a file. The difference between one arrow and two is the difference between starting over and adding to what is there.

---

## 1. Overwriting with `>`

A single `>` redirects a command's output into a file, **replacing its entire contents**.

```bash
$ mkdir -p design
$ echo "Level 01 - Drowned Gallery" > design/level-notes.txt
$ cat design/level-notes.txt
Level 01 - Drowned Gallery
```

The file is created if it does not exist. And if it does exist, its previous contents are gone:

```bash
$ echo "  - Boss: Guardian of Time" >> design/level-notes.txt
$ echo "  - Loot: Ember Blade" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 01 - Drowned Gallery
  - Boss: Guardian of Time
  - Loot: Ember Blade

$ echo "Level 02 - Collapsed Nave" > design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
```

Three lines became one. Nothing warned you.

> ⚠️ **Warning:** `>` is unconditional. There is no prompt, no backup, and no undo — the shell does not know that the previous contents mattered. Any command with `>` can destroy a file, including `cp` and `mv`.

---

## 2. Appending with `>>`

Two arrows add to the end of the file instead of replacing it.

```bash
$ echo "  - Hazard: Drowning" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
```

The first line survived. That is the whole difference:

| Operator | Existing file | Missing file |
| :--- | :--- | :--- |
| `>` | Contents **replaced** | Created |
| `>>` | Lines **added** at the end | Created |

> **Trap:** Both operators add a trailing newline, which is why `echo` pairs cleanly with them. Using `printf` without `\n` produces a file whose last line runs into the next one.

---

## 3. Combining Files with `cat`

Because redirection captures *output*, it works on any command that prints — including `cat` itself. That makes `cat` a file concatenator on disk:

```bash
$ cat design/level-notes.txt saves/slot-1.dat > design/merged.txt
$ cat design/merged.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
player: Kaela
level: 02
hp: 78
embers: 340
```

Swap the operator to append instead of replace:

```bash
$ cat saves/slot-2.dat >> design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
player: Roen
level: 05
hp: 41
embers: 1
```

And with several sources at once:

```bash
$ cat saves/slot-1.dat saves/slot-2.dat > design/all-runs.txt
```

> **Trap:** Using `>` with a source file that is also the destination truncates it before the read happens, so the result is empty. `cat notes.txt > notes.txt` produces an empty file. The safe form for rearranging a single file is a temporary name, or an append with `>>`.

---

## 4. Building a Notes File

The everyday version of all of the above, where each fact is one appended line:

```bash
$ mkdir -p design
$ echo "Level 03 - Ember Archive" > design/level-notes.txt
$ echo "  - Boss: Warden of Ash" >> design/level-notes.txt
$ echo "  - Loot: Ember Blade" >> design/level-notes.txt
$ echo "  - Loot: 3 health flasks" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 03 - Ember Archive
  - Boss: Warden of Ash
  - Loot: Ember Blade
  - Loot: 3 health flasks
```

The pattern is worth internalizing: the **first** write uses `>` because the file must be reset, and every **subsequent** write uses `>>` because it must accumulate. Getting the first one wrong leaves old content above your new entry; getting a later one wrong erases everything written so far.

---

## Key Takeaways

- `>` replaces a file's entire contents; `>>` appends to them. Both create the file if missing.
- Redirection captures output, so it works with any printing command — `cat` included.
- `cat a b > c` concatenates files on disk; `cat a b >> c` appends them to an existing file.
- Never redirect a file into itself with `>`; the result is empty.
- Build multi-line files with one `>` followed by many `>>`.

---
