
# 07. Project Blueprints

**Spanish version:** [07 - Planos del Proyecto.md](07%20-%20Planos%20del%20Proyecto.md)

**Course:** Command Line
**Topic:** Creating Directories with `mkdir` and the `-p` Flag
**Tags:** `#cli` `#mkdir` `#directories` `#file-management` `#project-structure`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Navigation commands let you explore a structure that already exists. Creating one is a different job: `mkdir` builds the folders, and the `-p` flag is what separates a one-level command from a whole tree.

---

## 1. Creating a Directory

`mkdir` — *make directory* — creates a folder at the given path.

### Syntax

```bash
mkdir <directory_name>
```

From the project root, a new folder for sound effects:

```bash
$ mkdir assets/sfx
$ ls assets
audio  maps  sfx  sprites
```

The new entry appears alongside the existing ones. The command did not move you into it — `mkdir` creates, `cd` enters. Keeping them separate is deliberate: you will often want to create several folders before entering any of them.

> **Note:** Creating a directory does not change your working directory. If you need to work inside it, follow with `cd` when you are ready.

---

## 2. The Common Error

`mkdir` will not create missing parents. Asking for a two-level path when only the first level exists fails:

```bash
$ mkdir nope/deeper
mkdir: nope: No such file or directory
```

The message names `nope`, not `deeper` — it is complaining about the **parent**, which is the part that does not exist. Read errors that way: they name the first thing they could not find.

The same message appears for a different mistake. Typing `cd` where `mkdir` belongs produces the identical wording:

```bash
$ cd build
cd: no such file or directory: build
```

> [!WARNING]
> **Trap**
> `no such file or directory` from `cd` means the folder is missing; from `mkdir` with a nested path it means the **parent** is missing. Same words, opposite fixes — `mkdir` the parent, or drop the nested part.

---

## 3. Nested Paths and the `-p` Flag

The `-p` flag tells `mkdir` to create every missing level in the path, not just the last one. It turns a two-step process into one:

```bash
$ mkdir builds/linux
mkdir: builds: No such file or directory

$ mkdir -p builds/linux builds/windows
$ ls builds
linux  windows
```

`mkdir -p` has two behaviours worth knowing:

- **Parents are created as needed.** Existing intermediate directories are simply left alone, so the command is safe to re-run.
- **It does not complain if the target already exists.** Unlike plain `mkdir`, which reports `File exists` and exits with an error.

That idempotence is what makes it the right choice in scripts:

```bash
$ mkdir assets
mkdir: assets: File exists

$ mkdir -p assets
$ echo "exit code: $?"
exit code: 0
```

> [!WARNING]
> **Trap**
> The leniency cuts both ways. `mkdir -p` will happily build a path with a typo in it, creating `builids/linux` and leaving you wondering why the build script ignores your new folder. The flag is not forgiving about *wrong*, only about *already there*.

---

## 4. Building a Build Matrix

Platform builds are the standard case for nested creation — each platform needs a directory, and the script should not care whether they already exist:

```bash
$ mkdir -p builds/linux builds/windows builds/macos builds/web
$ ls builds
linux  macos  web  windows
```

One command, four directories, safe to run every build. This is the pattern to reach for whenever a directory tree is described in a build script rather than created by hand.

---

## 5. Verifying the Result

Creation commands report nothing on success. Confirm the structure with a listing:

```bash
$ ls -R builds
linux
macos
web
windows

builds/linux:

builds/macos:

builds/web:

builds/windows:
```

`ls -R` lists the entries of each directory and then descends into the subdirectories, labelling each one with its full path. It is the fastest way to check a whole tree you just created — and notice that the four subdirectories are empty, which is exactly what this listing is telling you.

---

## Key Takeaways

- `mkdir <name>` creates one directory and does not move you into it.
- `mkdir` fails when the parent is missing — the error names the parent, not the target.
- `mkdir -p` creates all missing levels, tolerates existing directories, and is safe to re-run.
- `mkdir -p` is the right choice in scripts; plain `mkdir` is fine by hand.
- Verify a new tree with `ls -R`.

---
