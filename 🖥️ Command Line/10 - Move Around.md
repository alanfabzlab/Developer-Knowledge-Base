
# 10. Move Around

**Spanish version:** [10 - Mover y Renombrar.md](10%20-%20Mover%20y%20Renombrar.md)

**Course:** Command Line
**Topic:** Moving, Renaming, and Deleting with `mv`, `rm`, and `rmdir`
**Tags:** `#cli` `#mv` `#rm` `#rmdir` `#file-management` `#deletion`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

This is the lesson with the sharpest edges in the module. `mv` is the most useful command here and `rm` is the most dangerous; both take the same two-argument shape, and knowing how the second argument is interpreted is what tells them apart.

---

## 1. Moving with `mv`

`mv` — *move* — relocates a file or directory.

### Syntax

```bash
mv <source> <destination>
```

The two destinations behave differently, and that difference is the key to the whole command.

**Into an existing directory** — the file moves in and keeps its name:

```bash
$ echo "Level 05 - Ashen Spire" > design/boss-notes.txt
$ mv design/boss-notes.txt assets/audio/
$ ls assets/audio
boss-notes.txt  door-open.ogg  hit.wav
```

**To a new name** — the item is renamed in place:

```bash
$ mv assets/audio/boss-notes.txt assets/audio/boss-tips.txt
$ ls assets/audio
boss-tips.txt  door-open.ogg  hit.wav
```

Nothing moved the second time. The only difference between the two calls is whether the destination already exists as a directory.

Directories move the same way, contents included:

```bash
$ mv builds/macos builds/darwin
$ ls builds
darwin  linux  web  windows
```

> **Trap:** A directory destination that does not exist is treated as a **new name**, not as a location. `mv saves saved` renames the folder; `mv saves archive/` fails unless `archive/` already exists. Create it first with `mkdir -p archive`.

---

## 2. Deleting Files with `rm`

`rm` — *remove* — deletes files permanently, immediately, and without confirmation.

```bash
$ mkdir -p design/levels
$ touch design/scratch.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt  scratch.txt

$ rm design/scratch.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt
```

Several at once:

```bash
$ touch design/a.txt design/b.txt
$ rm design/a.txt design/b.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt
```

There is no `-i` prompt by default, and no trash folder. The file is gone.

> ⚠️ **Warning:** `rm` bypasses the system trash entirely. There is no undo, no confirmation, and no second chance — a mistyped path deletes the wrong file, and a mistyped flag can delete far more than intended. Always `ls` the target immediately before removing it.

---

## 3. Deleting Directories with `rmdir`

`rmdir` removes a directory, but **only if it is empty**. That restriction is a safety feature, and it is the reason to prefer it over `rm -r` for routine cleanup.

```bash
$ mkdir -p tmpdir
$ rmdir tmpdir
```

Several at once, which is handy for cleaning up a run of empty build directories:

```bash
$ mkdir -p x1 x2 x3
$ rmdir x1 x2 x3
$ echo "exit code: $?"
exit code: 0
```

Against a directory with contents, it refuses:

```bash
$ rmdir design
rmdir: design: Directory not empty
```

That refusal is the point. You cannot accidentally delete a populated project folder with `rmdir`, because the command will not try.

---

## 4. Recursive Removal with `rm -r`

When a directory is genuinely empty of nothing, `-r` removes it along with every file and subdirectory inside it.

```bash
$ rm -r builds/web
$ ls builds
darwin  linux  windows
```

> ⚠️ **Warning:** `rm -r` is the command to type carefully and never paste from an unverified source. The recursive flag removes *everything* below the target, without asking. Confirm the path with `pwd` and inspect it with `ls` first — the two seconds that costs is the difference between a cleanup and a lost afternoon.

The habit that makes it safe: navigate to the parent and list before deleting.

```bash
$ cd builds
$ ls
darwin  linux  windows
$ rm -r windows
$ ls
darwin  linux
```

---

## Key Takeaways

- `mv source dest` moves into a directory if it exists, and renames if it does not.
- `rm` deletes files permanently, with no prompt and no trash.
- `rmdir` deletes only empty directories — its refusal is a safety feature.
- `rm -r` removes a directory and everything under it; verify the path before running it.
- List the target immediately before any deletion.

---
