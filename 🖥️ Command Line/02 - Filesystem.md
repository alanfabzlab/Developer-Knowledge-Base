
# 02. Filesystem

**Spanish version:** [02 - Sistema de Archivos.md](02%20-%20Sistema%20de%20Archivos.md)

**Course:** Command Line
**Topic:** Directories, Files, Paths & `pwd`
**Tags:** `#cli` `#filesystem` `#paths` `#pwd` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

A filesystem is a tree. Everything the machine stores — your game project, a save file, a font — hangs off a single root. Learning to read that tree is the skill the rest of this module builds on.

---

## 1. The Three Shapes

Every entry in a filesystem is one of three things:

- **A file** — holds data. `player.gd`, `save.dat`, `theme.ogg`.
- **A directory** — holds other entries. Also called a *folder*; the two words mean the same thing.
- **A link** — a pointer to something that lives somewhere else. We will not need these until file management, but knowing they exist prevents surprises when a file turns out to live in a different place than its name suggests.

Directories exist purely to group. `scripts/` and `assets/` hold the same kind of thing in one case and different things in the other — the grouping is a decision you make, not a rule the system imposes.

---

## 2. The Project Tree

This module uses one workspace throughout, the source folder of a 2D game called **Sunken Keep**:

```text
SunkenKeep/
├── README.md
├── assets/
│   ├── audio/
│   │   ├── door-open.ogg
│   │   └── hit.wav
│   ├── sprites/
│   │   ├── hero.png
│   │   └── lantern.png
│   └── maps/
│       └── level-01.tmx
├── src/
│   ├── main.gd
│   └── player.gd
└── saves/
    ├── slot-1.dat
    └── slot-2.dat
```

Read it as nested pairs: `assets/` contains `audio/`, which contains `door-open.ogg`. That is the entire mental model — everything else is detail.

---

## 3. Finding Where You Are

`pwd` — *print working directory* — prints the absolute path of wherever you currently are.

```bash
$ pwd
/Users/dev/SunkenKeep/assets
```

The output breaks into three readable parts:

| Part | Value | Meaning |
| :--- | :--- | :--- |
| `/` | root | The single entry every path starts from |
| `/Users/dev/SunkenKeep` | home | Your user folder |
| `assets` | current | Where you are right now |

> **Trap:** `pwd` has no arguments. Anything you pass it is ignored, so `pwd assets` prints the same line as `pwd` — and if you think it moved you, your next command lands in the wrong directory.

---

## 4. Absolute vs. Relative Paths

Two ways to name the same place, and confusing them is the single most common source of "command did nothing".

**Absolute** — starts at root. Works from anywhere.

```bash
$ cat /Users/dev/SunkenKeep/saves/slot-1.dat
```

**Relative** — starts from where you are. Only works from here.

```bash
$ cat ../saves/slot-1.dat
```

In a relative path, `.` means *this directory* and `..` means *the parent*. The leading `../` in the second example is how you climb out of `assets/` and into `saves/`.

> **Trap:** A relative path is resolved against your **current directory**, which changes the moment you `cd`. A command that worked five minutes ago can quietly point somewhere else now. When in doubt, ask `pwd`.

---

## 5. Spaces in Names

Paths containing spaces must be quoted as a whole, or the shell will read the space as a separator and treat half the name as a second argument.

```bash
$ cd "My Game Assets"
```

> **Trap:** This bites in reverse too. `cd My Game Assets` fails because the shell tries to enter a directory called `My`. Prefer `snake_case` or `kebab-case` for project directories and sidestep the issue entirely — game engines and version control both prefer it anyway.

---

## Key Takeaways

- A filesystem is a tree of files, directories, and links rooted at `/`.
- `pwd` prints your absolute location and takes no arguments.
- Absolute paths work anywhere; relative paths depend on your current directory.
- `..` climbs to the parent, `.` stays put, and quoted paths handle spaces.

---
