
# 04. Reading the Keep

**Spanish version:** [04 - Leyendo la Mazmorra.md](04%20-%20Leyendo%20la%20Mazmorra.md)

**Course:** Command Line
**Topic:** Parent Paths, Absolute Paths & Reading Files with `cat`
**Tags:** `#cli` `#cat` `#relative-paths` `#navigation` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Chapter 1 finishes here. You can move, you can look, and now you will learn to read the actual contents of a file — the first time the terminal gives you something back other than a directory listing.

---

## 1. Climbing with `..`

From inside `assets/sprites/`, the parent is one `..` up:

```bash
$ cd ..
$ pwd
/Users/dev/SunkenKeep/assets
```

Chain them to climb several levels in one command. From `assets/sprites/`, reaching the project root takes two:

```bash
$ cd ../..
$ pwd
/Users/dev/SunkenKeep
```

The rule is mechanical: one `..` per level of depth. If you are three directories deep and need the root, you need three.

> [!WARNING]
> **Trap**
> Climbing above `/` is not possible. From `/`, `cd ..` leaves you at `/` and reports nothing — the filesystem root is its own parent.

---

## 2. Combining `.` and `..`

Real paths mix forward steps and climbs. A single `/` separates each part:

```bash
$ cd assets/maps
$ cd ../../saves
$ pwd
/Users/dev/SunkenKeep/saves
```

Here the path climbs two levels out of `assets/maps/` and steps back down into `saves/`. Read any such path left to right as instructions, and it stops being mysterious:

> out, out, down into `saves/`.

A lone `.` means *stay in the current directory*. It is rare in practice, but it appears in path arithmetic like `./build.sh` — the shell spells out "this directory" so the path is unambiguously relative.

---

## 3. Reading a File with `cat`

`cat` — *concatenate* — prints the contents of a file to the terminal. This is where the shell stops being a filing cabinet and starts being a reader.

```bash
$ cat saves/slot-1.dat
player: Kaela
level: 02
hp: 78
embers: 340
```

Several files can be printed one after another, which is why the command is named *concatenate*:

```bash
$ cat saves/slot-1.dat saves/slot-2.dat
player: Kaela
level: 02
hp: 78
embers: 340
player: Roen
level: 05
hp: 41
embers: 1
```

Both save files print one after the other, with no separator. That is precisely what *concatenate* means, and it is why `cat` is better at reading than at combining — for that, redirect the output instead, as in [[09 - Writing the Lore]].

> [!WARNING]
> **Trap**
> `cat` on a directory reports `Is a directory`. And on a large file — a generated asset dump, a log with ten thousand lines — it floods your terminal with no way to stop early. `head` shows just the first few lines, `tail` the last, and `less` pages through it. Reach for those when a file is large.

---

## 4. Why Paths Need Quoting

Any path with a space in it must be quoted, or the shell splits it into separate arguments and the command fails:

```bash
$ cd assets
$ cat "audio files/long-jump.ogg"
```

The quotes tell the shell to treat everything between them as one name. Without them, `audio` and `files/long-jump.ogg` become two separate arguments and `cat` looks for a file called `audio`.

---

## Key Takeaways

- `..` climbs one level; chain it to climb several. `/` is the root and its own parent.
- `.` means the current directory and makes relative paths explicit.
- `cat` prints file contents to the terminal and accepts several files at once.
- Use `head`, `tail`, or `less` instead of `cat` on anything large.
- Paths with spaces must be quoted in full.

---
