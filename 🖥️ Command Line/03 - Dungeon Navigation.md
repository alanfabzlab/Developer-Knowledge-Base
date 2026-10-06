
# 03. Dungeon Navigation

**Spanish version:** [03 - Navegando la Mazmorra.md](03%20-%20Navegando%20la%20Mazmorra.md)

**Course:** Command Line
**Topic:** Changing Directory & Listing Contents
**Tags:** `#cli` `#cd` `#ls` `#navigation` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Knowing where you are is half of navigation. This lesson covers the other half: moving between directories and seeing what is inside them before you commit to anything.

---

## 1. Moving with `cd`

`cd` — *change directory* — moves your shell into a directory. It changes the shell's working directory and nothing else: no file is touched, and your previous location is not recorded anywhere.

```bash
$ cd /Users/dev/SunkenKeep
$ cd assets
$ cd sprites
```

Moving down one level at a time, as above, is readable but tedious. You can also name the whole path at once, from anywhere:

```bash
$ cd /Users/dev/SunkenKeep/assets/audio
```

To return home, the tilde is shorthand for your user directory:

```bash
$ cd ~
```

And to come back to where you started, `cd -` swaps to the directory you were in before the last move:

```bash
$ cd ..
$ cd -
/Users/dev/SunkenKeep/assets
```

> [!WARNING]
> **Trap**
> `cd` cannot create anything. Typing `cd build` into a directory that does not exist reports `no such file or directory` — and the fix is `mkdir build`, covered in [[07 - Project Blueprints]]. The two errors share a message but mean opposite things.

---

## 2. Listing with `ls`

`ls` — *list* — prints the contents of the current directory.

```bash
$ ls
assets  README.md  saves  src
```

That single line is the whole project at a glance. The problem is that plain `ls` tells you nothing about the entries themselves: no type, no size, no date.

Two flags fix that:

```bash
$ ls -l
total 24
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src
```

Add `-a` and the two entries nobody remembers come into view:

```bash
$ ls -la
total 32
drwxr-xr-x  6 dev  staff   192 Jan  9 09:14 .
drwxr-xr-x  3 dev  staff    96 Jan  9 09:14 ..
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src
```

| Flag | Shows |
| :--- | :--- |
| `-l` | Long format: permissions, owner, size, date |
| `-a` | All, including entries starting with `.` |

The first character of each line is the type: `-` for a file, `d` for a directory. `drwxr-xr-x` on `assets` is your confirmation that it is a folder.

> [!WARNING]
> **Trap**
> `ll` is not `ls -l` on macOS. Some Linux distributions define it as an alias; macOS does not, and the shell reports `command not found`. Type the flags out.

---

## 3. One Flag, Many Items

`ls` accepts several paths at once, which saves a round trip when checking two branches of the project:

```bash
$ ls -l src saves
saves:
total 16
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 slot-1.dat
-rw-r--r--  1 dev  staff  40 Jan  9 09:14 slot-2.dat

src:
total 16
-rw-r--r--  1 dev  staff  15 Jan  9 09:14 main.gd
-rw-r--r--  1 dev  staff  24 Jan  9 09:14 player.gd
```

Note that `ls` labels each group with its directory name before listing that group's contents. When you pass several paths, the labels are what make the output readable — an unlabelled wall of filenames would be ambiguous.

This also works on files, not just directories — handy for comparing a stale build against the current one:

```bash
$ ls -l src/main.gd saves/slot-1.dat
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 saves/slot-1.dat
-rw-r--r--  1 dev  staff  15 Jan  9 09:14 src/main.gd
```

When every argument is a file, no directory labels are needed — the paths say which is which. Note the order: `ls` sorts by name, so `saves/` precedes `src/` regardless of the order you typed the arguments.

---

## Key Takeaways

- `cd` moves the working directory; `cd ~` goes home and `cd -` returns to the previous one.
- `cd` never creates anything — a missing directory means `mkdir`.
- `ls -l` adds permissions, size, and date; the leading `-` or `d` reveals file versus directory.
- `ls -a` reveals dotfiles, where `.git` and editor configs live.
- Several paths can be listed in a single `ls` call.

---
