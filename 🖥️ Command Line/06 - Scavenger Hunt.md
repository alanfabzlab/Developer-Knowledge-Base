
# 06. Scavenger Hunt

**Spanish version:** [06 - Búsqueda del Tesoro.md](06%20-%20B%C3%BAsqueda%20del%20Tesoro.md)

**Course:** Command Line
**Topic:** Chapter 1 Review & Navigation Challenge
**Tags:** `#cli` `#review` `#challenge` `#navigation` `#filesystem`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Chapter 1 is navigation: knowing where you are, moving, looking, and reading. This is a checkpoint — a scavenger hunt through the project that uses every command from the first five lessons, in the order you would actually reach for them.

---

## 1. Chapter 1 Command Summary

| Command | Syntax | Description |
| :--- | :--- | :--- |
| `echo` | `echo [text]` | Prints text to standard output |
| `pwd` | `pwd` | Prints the absolute path of the working directory |
| `ls` | `ls [path]` | Lists the entries in a directory |
| `ls -l` | `ls -l [path]` | Long format: permissions, owner, size, date |
| `ls -a` | `ls -a [path]` | Includes entries whose names start with `.` |
| `cd` | `cd [directory]` | Moves into a directory |
| `cd ..` | `cd ..` | Moves up to the parent directory |
| `cd ~` | `cd ~` | Moves to your home directory |
| `cd -` | `cd -` | Returns to the previous directory |
| `cat` | `cat [file]` | Prints a file's contents |
| `clear` | `clear` | Clears the visible screen |
| `Tab` | `Tab` | Completes a command or path |

---

## 2. The Clues

Work from the project root and answer each one using the command that fits. If a step needs more than you have learned, that is the clue that you skipped something.

1. Where am I, exactly? Print the full path.
2. What is at the top level of the project? List it.
3. Which of those are directories rather than files? Show type, size, and date.
4. Is there anything here whose name starts with a dot? Include hidden entries.
5. Into which directory do I move to reach the sprite files?
6. How do I get to the parent of the directory I am in now?
7. How do I return to the directory I was in before that?
8. Print the contents of the first save file without opening an editor.
9. Print both save files one after the other.
10. What is in the maps directory?
11. Clear the screen without losing my location. Where am I afterwards?
12. Complete `cd SunkenKeep/assets/a` into a full directory name using one key.

---

## 3. A Walkthrough

One route through the hunt, with the output each step produces:

```bash
$ pwd
/Users/dev/SunkenKeep

$ ls
README.md  assets  saves  src

$ ls -l
total 24
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src

$ ls -la
total 32
drwxr-xr-x  6 dev  staff   192 Jan  9 09:14 .
drwxr-xr-x  3 dev  staff    96 Jan  9 09:14 ..
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src

$ cd assets/sprites
$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ cd ..
$ pwd
/Users/dev/SunkenKeep/assets

$ cd -
/Users/dev/SunkenKeep/assets/sprites

$ cat ../../saves/slot-1.dat
player: Kaela
level: 02
hp: 78
embers: 340

$ cat ../../saves/slot-1.dat ../../saves/slot-2.dat
player: Kaela
level: 02
hp: 78
embers: 340
player: Roen
level: 05
hp: 41
embers: 1

$ ls ../maps
level-01.tmx

$ clear

$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ cd SunkenKeep/assets/a<Tab>
cd: no such file or directory

$ pwd
/Users/dev/SunkenKeep/assets/sprites
```

That last step is worth pausing on: `Tab` completed the name perfectly and the command still failed, because the terminal was already inside `SunkenKeep`. A relative path only resolves from where you are — the rule from [[02 - Filesystem]] showing up exactly where it tends to bite.

The second `pwd` is the point of the clue. A failed `cd` leaves you exactly where you were, which is why checking your location after a mistake is a habit worth keeping.

> [!warning] Trap
> `cd -` toggles between the last two directories, so running it twice returns you to where you started. It is also the easiest way to end up somewhere you did not mean to be, since it overrides wherever your `cd` was heading.

---

## Key Takeaways

- Chapter 1 gave you six verbs: `pwd` to locate, `ls` to look, `cd` to move, `cat` to read, `clear` to reset the view, `Tab` to type less.
- `cd -` toggles between the last two directories and will override an intended `cd`.
- Relative paths resolve against the current directory, which changes with every `cd`.
- Always print a listing before deleting anything — that habit starts in this chapter.

---
