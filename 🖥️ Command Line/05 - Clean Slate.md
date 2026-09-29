
# 05. Clean Slate

**Spanish version:** [05 - Hoja en Blanco.md](05%20-%20Hoja%20en%20Blanco.md)

**Course:** Command Line
**Topic:** Clearing the Screen, Command History & Tab Completion
**Tags:** `#cli` `#clear` `#history` `#tab-completion` `#productivity`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

A long session fills the terminal with output until the command you care about is somewhere in the middle. This lesson is about keeping the screen readable and your hands off the keyboard.

---

## 1. Clearing the Screen

`clear` wipes the visible text and leaves you with a fresh prompt at the top.

```bash
$ clear
```

That is the whole command. It takes no arguments and does no work to your files.

> **Important:** `clear` only redraws what you see. It does **not** move you, delete anything, or reset environment variables. Your working directory is exactly where it was before.

To prove it, clear from deep inside the project and check immediately afterwards:

```bash
$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ clear

$ pwd
/Users/dev/SunkenKeep/assets/sprites
```

The screen is blank, the location is unchanged. A blank terminal is a cosmetic reset, not a new session.

---

## 2. Command History

The shell logs every command you run in the current session. The arrow keys walk through that log.

| Key | Action |
| :--- | :--- |
| `↑` | Move back to the previous command |
| `↓` | Move forward to the next command |

Press `↑` repeatedly to scroll backwards, stop on the command you want, and edit it before running. Retyping a long path wastes effort the shell already spent remembering it.

### Searching Instead of Scrolling

When the log is long, `Ctrl + R` is faster than arrowing. Type a fragment and the shell searches your history for the first match:

```text
$ Ctrl + R, then type "slot"
(reverse-i-search)`slot': cat saves/slot-1.dat
```

Press `Enter` to run it, or `Ctrl + R` again to look for the next match.

> [!WARNING]
> **Trap**
> History is per session. Close the terminal and the log is gone — there is no way to recover a command from a session you already ended.

---

## 3. Tab Completion

The `Tab` key completes what you have typed so far. Press it once and the shell fills in the rest; press it twice and it lists every candidate that shares your prefix.

Tab-completing a directory name:

```text
$ cd Sun<Tab>
$ cd SunkenKeep/

$ cd SunkenKeep/src/<Tab><Tab>
config/  player.gd  main.gd
```

That second example is the useful one: two presses show you every option instead of guessing, which is how you discover a `config/` directory you forgot existed.

Completion applies to command names, file names, and directory paths — which makes long project paths a two-keystroke affair.

> [!WARNING]
> **Trap**
> If nothing completes, there is no match for what you typed. The most common cause is being in the wrong directory; a path that resolves from somewhere else looks identical here. Confirm with `pwd`.

---

## 4. A Shortcut Worth Building

A three-step session, done the fast way:

```bash
$ cd Sun<Tab>
$ ls -la as<Tab><Tab>
$ cat assets/maps/level-01.tmx
```

The first two lines cost four keystrokes. Typing them out costs roughly forty. This is the payoff of the whole chapter: the terminal is not faster because typing is fast, but because the shell finishes your sentences.

---

## Key Takeaways

- `clear` wipes the visible screen only — location, files, and variables are untouched.
- `↑` and `↓` walk the session's command history; `Ctrl + R` searches it.
- `Tab` completes commands and paths; `Tab` twice lists every candidate.
- History does not survive the session, so capture anything you need before closing.

---
