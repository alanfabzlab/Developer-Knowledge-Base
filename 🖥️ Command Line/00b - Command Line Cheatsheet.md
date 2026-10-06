
# 00b. Command Line Cheatsheet

**Spanish version:** [00b - Chuleta de Línea de Comandos.md](00b%20-%20Chuleta%20de%20L%C3%ADnea%20de%20Comandos.md)

**Course:** Command Line
**Topic:** Complete Reference for Navigation, File Management, Redirection & Shortcuts
**Tags:** `#cli` `#cheatsheet` `#reference` `#bash` `#terminal`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

One-page reference for the whole module. Examples use the **Sunken Keep** project tree introduced in [[02 - The Project Tree]].

---

## 🧭 Navigation & Traversal

| Task | Command | Example |
| :--- | :--- | :--- |
| **Print working directory** | `pwd` | `pwd` |
| **List contents** | `ls` | `ls` |
| **Long listing** | `ls -l` | `ls -l` |
| **Include hidden entries** | `ls -a` | `ls -la` |
| **List recursively** | `ls -R` | `ls -R content` |
| **Change directory** | `cd` | `cd assets` |
| **Up one level** | `cd ..` | `cd ..` |
| **Up two levels** | `cd ../..` | `cd ../..` |
| **Go home** | `cd ~` | `cd ~` |
| **Return to previous** | `cd -` | `cd -` |
| **Change to root** | `cd /` | `cd /` |

---

## 📁 Creating Files & Directories

| Task | Command | Example |
| :--- | :--- | :--- |
| **Make a directory** | `mkdir` | `mkdir assets/sfx` |
| **Make nested directories** | `mkdir -p` | `mkdir -p builds/linux builds/win` |
| **Create an empty file** | `touch` | `touch src/enemy.gd` |
| **Create several files** | `touch` | `touch src/a.gd src/b.gd` |
| **Keep an empty directory** | `touch` | `touch assets/sfx/.gitkeep` |

---

## ✍️ Text & Redirection Streams

| Task | Command | Example |
| :--- | :--- | :--- |
| **Print text** | `echo` | `echo "Level 01"` |
| **Overwrite file with text** | `echo >` | `echo "Level 01" > notes.txt` |
| **Append text to file** | `echo >>` | `echo "  - Boss" >> notes.txt` |
| **Print a file** | `cat` | `cat notes.txt` |
| **Overwrite file with file** | `cat >` | `cat a.txt > b.txt` |
| **Append file to file** | `cat >>` | `cat a.txt >> b.txt` |
| **First lines of a file** | `head` | `head -5 notes.txt` |
| **Last lines of a file** | `tail` | `tail -5 notes.txt` |
| **Page through a file** | `less` | `less notes.txt` |
| **Count lines** | `wc -l` | `wc -l notes.txt` |
| **Search text in files** | `grep` | `grep -r "Ember" src/` |

---

## 📦 Moving, Copying & Removing

| Task | Command | Example |
| :--- | :--- | :--- |
| **Move / rename** | `mv` | `mv old-name new-name` |
| **Move into a directory** | `mv` | `mv notes.txt design/` |
| **Copy a file** | `cp` | `cp notes.txt notes.bak` |
| **Copy a directory** | `cp -r` | `cp -r saves saves-backup` |
| **Remove a file** | `rm` | `rm notes.txt` |
| **Remove an empty directory** | `rmdir` | `rmdir tmpdir` |
| **Remove a directory recursively** | `rm -r` | `rm -r builds/web` |
| **Confirm before removing** | `rm -i` | `rm -i notes.txt` |

> ⚠️ `rm` and `rm -r` are permanent. Run `ls` on the target first.

---

## ⌨️ Shortcuts & Terminal Utilities

| Shortcut / Utility | Action |
| :--- | :--- |
| **`Tab`** | Autocompletes commands, files, and paths |
| **`Tab` `Tab`** | Lists every candidate for the prefix |
| **`↑` / `↓`** | Walks command history |
| **`Ctrl` + `R`** | Reverse-searches history by fragment |
| **`Ctrl` + `C`** | Cancels the running command |
| **`Ctrl` + `A` / `E`** | Moves to the start / end of the line |
| **`Ctrl` + `L`** | Clears the screen (same as `clear`) |
| `clear` | Clears the visible screen only |
| `say "text"` | macOS: reads the text aloud |
| `open .` | macOS: opens the current directory in Finder |
| `pbcopy` / `pbpaste` | macOS: copies to / reads from the clipboard |

---

## 🚦 The Order of Operations

When unsure which command to reach for:

| You want to… | Reach for |
| :--- | :--- |
| See where you are | `pwd` |
| See what is here | `ls` |
| See the whole tree | `ls -R` |
| Go somewhere | `cd` |
| Read a file | `cat` (or `less` if large) |
| Make a folder | `mkdir -p` |
| Make a file | `touch` |
| Write a file fresh | `>` |
| Add to a file | `>>` |
| Relocate or rename | `mv` |
| Duplicate first | `cp` |
| Delete a file | `rm` |
| Delete an empty folder | `rmdir` |
| Delete a folder with contents | `rm -r` (after `ls`) |

---

## ⚠️ The Traps Worth Memorizing

| Mistake | What happens |
| :--- | :--- |
| `cd build` when it does not exist | Fails — you must `mkdir` it first |
| `mkdir a/b` when `a` is missing | Fails — the error names the **parent** |
| `mkdir` an existing directory | Reports `File exists`; use `-p` |
| `touch new-dir/file.txt` | Fails — `touch` does not create directories |
| `cat a > a` | Truncates the file before reading it — result is empty |
| `cp a a` | Same self-overwrite trap |
| `echo "x" > notes.txt` twice | The second call erases the first |
| Unquoted path with a space | The shell splits it into two arguments |
| `rm -r` without `ls` first | Everything under that path is gone |
| Trusting `cd -` blindly | It toggles between the last two directories |
