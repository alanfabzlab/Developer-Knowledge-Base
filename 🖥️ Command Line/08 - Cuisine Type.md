
# 08. Forging Files

**Spanish version:** [08 - Tipo de Cocina.md](08%20-%20Tipo%20de%20Cocina.md)

**Course:** Command Line
**Topic:** Creating Files with `touch` and File Extensions
**Tags:** `#cli` `#touch` `#files` `#extensions` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

`mkdir` builds the folders; `touch` creates the files inside them. This is the command that lets you reserve a filename before it has any contents — and the extension on that name is a decision your tools will read later.

---

## 1. Creating a File

`touch` creates an empty file at the given path.

### Syntax

```bash
touch <file_name>
```

```bash
$ touch saves/slot-3.dat
$ ls -l saves
total 16
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 slot-1.dat
-rw-r--r--  1 dev  staff  40 Jan  9 09:14 slot-2.dat
-rw-r--r--  1 dev  staff   0 Jan  9 09:14 slot-3.dat
```

The size is `0`. The file exists, the contents do not — which is exactly what you want when a tool refuses to save because the output path is missing.

> **Note:** If the file already exists, `touch` updates its modification time and leaves the contents alone. It cannot accidentally empty a file.

---

## 2. Extensions Are Naming Convention

The shell treats `hero.png` and `hero` as unrelated names. What makes a file an image, a script, or audio is the **extension** — the text after the final dot.

| Extension | Typical role in a game project |
| :--- | :--- |
| `.gd` | Gameplay script |
| `.tscn` | Scene definition |
| `.tmx` | Tiled map data |
| `.png` | Sprite or UI image |
| `.ogg` / `.wav` | Sound effect or music |
| `.dat` | Save or serialized state |
| `.json` | Configuration or data table |
| `.md` | Documentation |

`touch` accepts any of them, because the shell does not interpret the extension — your editor, engine, and version control do.

```bash
$ touch src/enemy.gd src/pickup.gd
$ ls src
enemy.gd  main.gd  pickup.gd  player.gd
```

Several paths in one command is the normal usage; there is no reason to run it four times.

---

## 3. Creating Across Subdirectories

The path can include existing directories, which is how a file lands in the right place without moving first:

```bash
$ touch assets/maps/level-02.tmx
$ ls assets/maps
level-01.tmx  level-02.tmx
```

> [!WARNING]
> **Trap**
> `touch` will not create the directories on the way. `touch new-folder/notes.txt` fails with `No such file or directory` when `new-folder` does not exist. Create the folder first with `mkdir -p new-folder`, then the file.

---

## 4. The Habit Worth Building

`touch` is most valuable as a reservation. Many tools refuse to create their own directory and will fail on a path that does not exist, so pre-creating the structure lets the tool do its job:

```bash
$ mkdir -p assets/sfx
$ touch assets/sfx/.gitkeep
$ ls -a assets/sfx
.  ..  .gitkeep
```

The empty `.gitkeep` holds the directory in version control, which otherwise ignores folders with no files inside. Same reason, different tool: a placeholder for something that must exist but has nothing to say yet.

---

## Key Takeaways

- `touch` creates an empty file; on an existing file it only updates the timestamp.
- Extensions are a naming convention the shell ignores and your engine reads.
- `touch` accepts several paths at once and can target existing subdirectories.
- It will not create missing parent directories — use `mkdir -p` first.
- An empty `.gitkeep` is the standard way to keep an empty directory under version control.

---
