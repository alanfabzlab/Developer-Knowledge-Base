
# 12. Dungeon Build

**Spanish version:** [12 - Listas de Reproducción.md](12%20-%20Listas%20de%20Reproducci%C3%B3n.md)

**Course:** Command Line
**Topic:** Chapter 2 Review, Recursive Listing & Full Workflow
**Tags:** `#cli` `#review` `#ls-R` `#workflow` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Chapter 2 dealt with changing the filesystem: creating, writing, moving, copying, deleting. This final exercise assembles all of it into the workflow you would actually run at the end of a session, and closes the module with `ls -R`, the command that shows you what you built.

---

## 1. Chapter 2 Command Review

| Command / Flag | Function |
| :--- | :--- |
| `mkdir` | Creates a directory |
| `mkdir -p` | Creates every missing level; safe to re-run |
| `touch` | Creates an empty file; updates the timestamp if it exists |
| `echo >` | Writes text to a file, replacing its contents |
| `echo >>` | Appends a line to a file |
| `cat >` | Writes a file's contents into another, replacing it |
| `cat >>` | Appends a file's contents to another |
| `mv` | Moves or renames a file or directory |
| `cp` | Copies a file |
| `cp -r` | Copies a directory and its contents |
| `rm` | Removes a file, permanently |
| `rmdir` | Removes an empty directory |
| `rm -r` | Removes a directory and everything under it |
| `ls -R` | Lists contents recursively across all subdirectories |

That is a complete file-management toolkit: **inspect** with `ls`, **create** with `mkdir` and `touch`, **write** with `>` and `>>`, **reorganize** with `mv`, **protect** with `cp`, **remove** with `rm` and `rmdir`.

---

## 2. Building a Level Workspace

Creating the structure for a new level, with nested directories in one command:

```bash
$ mkdir -p content/levels/01-drowned-gallery
$ mkdir -p content/assets/levels/01-drowned-gallery
$ mkdir -p content/scripts/enemies
$ ls -R content
assets
levels
scripts

content/assets:
levels

content/assets/levels:
01-drowned-gallery

content/assets/levels/01-drowned-gallery:

content/levels:
01-drowned-gallery

content/levels/01-drowned-gallery:

content/scripts:
enemies

content/scripts/enemies:
```

Note the empty level directory. `mkdir -p` produced it, and it will not survive a version-control commit on its own — the `.gitkeep` trick from [[08 - Cuisine Type|08. Forging Files]] applies.

---

## 3. Populating with Notes

Every write after the first uses `>>`, so the file accumulates:

```bash
$ echo "Drowned Gallery" > content/levels/01-drowned-gallery/notes.txt
$ echo "  - Boss: Guardian of Time" >> content/levels/01-drowned-gallery/notes.txt
$ echo "  - Loot: Ember Blade" >> content/levels/01-drowned-gallery/notes.txt
$ echo "  - Enemies: 6 drowned wraiths" >> content/levels/01-drowned-gallery/notes.txt
$ cat content/levels/01-drowned-gallery/notes.txt
Drowned Gallery
  - Boss: Guardian of Time
  - Loot: Ember Blade
  - Enemies: 6 drowned wraiths
```

Adding an enemy script by path, without moving there first:

```bash
$ touch content/scripts/enemies/drowned-wraith.gd
$ ls content/scripts/enemies
drowned-wraith.gd
```

---

## 4. Reorganizing and Backing Up

The rearrangement half of a session, in the order you would actually run it:

```bash
$ cp -r content/levels content/levels-backup
$ mv content/levels/01-drowned-gallery content/levels/02-collapsed-nave
$ mkdir -p content/levels/01-drowned-gallery
$ ls content/levels
01-drowned-gallery  02-collapsed-nave
```

The copy is a safety net for the `mv` that follows it. When the move turns out to be wrong, the backup is already there.

---

## 5. Verifying the Whole Tree

`ls -R` — *recursive list* — walks every subdirectory and prints the full hierarchy:

```bash
$ ls -R content
assets
levels
levels-backup
scripts

content/assets:
levels

content/assets/levels:
01-drowned-gallery

content/assets/levels/01-drowned-gallery:

content/levels:
01-drowned-gallery
02-collapsed-nave

content/levels/01-drowned-gallery:

content/levels/02-collapsed-nave:
notes.txt

content/levels-backup:
01-drowned-gallery

content/levels-backup/01-drowned-gallery:
notes.txt

content/scripts:
enemies

content/scripts/enemies:
drowned-wraith.gd
```

Read it as an indented tree: each block is one directory, and the repeated prefix is the full path of its parent. It is the closest thing the terminal has to a visual map of a project.

Note the new `01-drowned-gallery` sits empty — `mv` carried its contents away, and the fresh `mkdir -p` put back only the folder. That is the usual way a level gets reset before being rebuilt.

> [!WARNING]
> **Trap**
> `ls -R` has no depth limit, so on a large project it can print thousands of lines. Add `| head -50` when you only want the shape, or `| less` to page through it.

---

## 6. Cleaning Up

Finishing the session without leaving debris:

```bash
$ rmdir content/levels/01-drowned-gallery
$ rm content/levels/02-collapsed-nave/notes.txt
$ rmdir content/levels/02-collapsed-nave
$ rm -r content/levels-backup
$ ls content
assets  levels  scripts
```

Four deletion commands for four different situations: an empty directory, a file, a directory that becomes empty once the file is gone, and a directory with contents that no command but `rm -r` will touch.

---

## Key Takeaways

- Chapter 2's toolkit is inspect, create, write, reorganize, protect, remove.
- `mkdir -p` builds nested trees; an empty directory still needs a `.gitkeep` to persist.
- Use `>` for the first write to a file and `>>` for every one after it.
- Copy before you move: `cp -r` first, `mv` second.
- `ls -R` is the verification step; pipe it through `head` on large trees.

---
