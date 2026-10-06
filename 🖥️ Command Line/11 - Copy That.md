
# 11. Copy That

**Spanish version:** [11 - Copia Eso.md](11%20-%20Copia%20Eso.md)

**Course:** Command Line
**Topic:** Duplicating Files and Directories with `cp` and `cp -r`
**Tags:** `#cli` `#cp` `#backup` `#file-management` `#duplication`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

`mv` relocates; `cp` duplicates. The syntax is identical, and the difference is that the original survives. That makes `cp` the safe command — the one to reach for when a backup matters more than a move.

---

## 1. Copying a File

`cp` — *copy* — writes a duplicate of the source to the destination.

### Syntax

```bash
cp <source_file> <destination_file>
```

Making a backup before an edit is the canonical use:

```bash
$ cp design/level-notes.txt design/level-notes.bak
$ ls design
all-runs.txt  level-notes.bak  level-notes.txt  levels  merged.txt
```

Both files now exist, and editing one does not touch the other.

### Key Behaviours

- **New file.** If the destination does not exist, it is created.
- **Existing file.** If it does exist, its contents are **replaced** by the source — with no prompt and no backup of what was there.
- **Directory destination.** If the destination is an existing directory, the file is copied **into** it under its original name.

```bash
$ mkdir -p design/archive
$ cp design/level-notes.txt design/archive/
$ ls design/archive
level-notes.txt
```

> [!WARNING]
> **Trap**
> The overwrite is the one to watch. `cp important.txt backup.txt` is harmless, but `cp important.txt important.txt` truncates the file before reading it — same self-overwrite trap as `cat a > a` in [[09 - Writing the Lore]].

---

## 2. Copying Directories with `cp -r`

`cp` on a directory reports `is a directory` and copies nothing. The `-r` flag makes it recurse, so the whole subtree comes along:

```bash
$ mkdir -p builds/darwin
$ touch builds/darwin/keep
$ cp -r builds/darwin builds/darwin-backup
$ ls builds
darwin  darwin-backup  linux

$ ls -R builds/darwin-backup
keep
```

`ls -R` is the verification step: it shows the copy actually contains what the original did, which is the only reason to trust a recursive copy.

### Where the Copy Lands

The destination rules mirror `mv`, with one addition:

| Destination | Result |
| :--- | :--- |
| New name | Copy is created under that name |
| Existing directory | Copy is nested **inside** it |
| Source and destination match | Refused: `are identical (not copied)` |

```bash
$ cp -r saves saves-backup
$ ls saves-backup
slot-1.dat  slot-2.dat  slot-3.dat
```

Nested into an existing folder:

```bash
$ mkdir -p backup
$ cp -r saves backup/
$ ls backup
saves
```

> [!WARNING]
> **Trap**
> Copying a directory into a directory that already contains a copy of it produces `builds/linux and builds/linux are identical (not copied)`. Harmless here, but it means the command did nothing while appearing to run — check where the files landed with `ls` before assuming a backup exists.

---

## 3. Backing Up a Directory

The pattern worth keeping: copy before you touch anything.

```bash
$ cp -r saves saves-backup
$ rm saves/slot-1.dat
$ ls saves
slot-2.dat  slot-3.dat

$ cp saves-backup/slot-1.dat saves/
$ ls saves
slot-1.dat  slot-2.dat  slot-3.dat
```

`rm` deleted the file with no confirmation and no trash, and the copy put it back. This is the entire argument for `cp` in a workflow that includes deletion: version control protects code, but an asset or save file outside the repository exists only where you put it.

---

## Key Takeaways

- `cp` duplicates a file, leaving the original in place; `mv` relocates.
- A new destination is created, an existing file is replaced, and an existing directory receives the copy inside it.
- `cp` on a directory does nothing without `-r`.
- `cp -r` follows the same destination rules and refuses to copy a directory onto itself.
- Copy before you delete — `rm` is unrecoverable and a copy is the only cheap insurance.

---
