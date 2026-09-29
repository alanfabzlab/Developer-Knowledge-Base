
# 01. In The Beginning

**Spanish version:** [01 - En los Orígenes.md](01%20-%20En%20los%20Or%C3%ADgenes.md)

**Course:** Command Line
**Topic:** Shell History, GUI vs. CLI, First Commands
**Tags:** `#cli` `#shell` `#basics` `#terminal` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Every shell session begins the same way: you open a window, and the machine waits for your instructions. This first lesson covers what the shell actually is, why it survives next to a polished GUI, and how to make it say something on your very first try.

---

## 1. What the Shell Is

The **shell** is a program that reads what you type, interprets it, and asks the operating system to carry it out. On macOS the default is **Zsh**; on older systems and much of Linux you will meet **Bash**. Both speak the same grammar, so everything in this module works in either one.

The word *shell* is literal: you type a command, the shell expands it, hands it to the system, and hands you back the result. Nothing is hidden behind a button.

---

## 2. Why the CLI Outlives the GUI

A graphical interface is a layer painted over the shell. The shell is the layer underneath it, which is why the terminal still wins in three situations:

- **Repetition.** Ten manual clicks become one command you can run a hundred times.
- **Precision.** A filename with a space in it is unambiguous when you quote it.
- **Remote work.** A server with no desktop is still fully usable.

> [!WARNING]
> **Trap**
> A GUI hides the filesystem. The shell shows it. That visibility is the whole point — and it is also why a mistyped `rm` can be just as unforgiving as a mistyped click.

---

## 3. Your First Command

`echo` prints its arguments and nothing more. It is the smallest possible proof that the shell is listening.

```bash
$ echo "Sunken Keep build 0.9.4 compiled"
Sunken Keep build 0.9.4 compiled
```

Without quotes, the shell splits your input on whitespace and `echo` rejoins the pieces with single spaces. The difference is visible once the text contains more than one gap:

```bash
$ echo Level   02 - Flooded Halls
Level 02 - Flooded Halls

$ echo "Level   02 - Flooded Halls"
Level   02 - Flooded Halls
```

> [!WARNING]
> **Trap**
> Quote anything with **two spaces in a row**, a **tab**, or a **special character** like `*` or `$`. Unquoted, those are expanded by the shell before `echo` ever sees them.

On macOS, `say` reads its argument out loud — genuinely useful when a build log needs your eyes on something else:

```bash
$ say "Level design linked successfully"
```

---

## 4. Reading the Prompt

Every command you type is preceded by a prompt. The default in this vault's examples is a plain `$`, which is a deliberate convention so the prompt never competes with the output:

```text
$ echo "hello"
hello
```

Two things worth knowing about real prompts:

- The text before `$` shows your **current directory** and your **git branch** — a free status display.
- The same command typed twice may show two different prompts and still do the same thing. The prompt is decoration; the command is the work.

---

## 5. Shell History

The shell keeps a log of everything you have run, and the arrow keys walk through it.

| Key | Action |
| :--- | :--- |
| `↑` | Previous command |
| `↓` | Next command |
| `Ctrl` + `R` | Search history by fragment |

Press `↑` repeatedly to walk backwards until you find the one you want, then edit it. Re-typing a long path is wasted work when the shell already remembers it for you.

> [!WARNING]
> **Trap**
> History is per shell session. The `history` command lists it, but a closed terminal discards it — there is no undo across sessions for a command that went wrong.

---

## Key Takeaways

- The shell interprets text and hands it to the operating system; the GUI is a layer on top of it.
- The CLI wins on repetition, precision, and remote work.
- Always quote text that contains double spaces, tabs, or shell metacharacters.
- Arrow keys and `Ctrl + R` turn your command history into a searchable log.

---
