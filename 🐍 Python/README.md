<div align="center">

# 🐍 Python: The Art of Algorithmic Craft (MOC)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Obsidian](https://img.shields.io/badge/Obsidian-483699?logo=obsidian&logoColor=white)](https://obsidian.md/)
[![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white)](https://www.apple.com/macos/)

_A dynamic knowledge map for transforming Python syntax into functional projects, architectures, and systems._

</div>

> [!NOTE]
> This page is the central map for the Python notes in this Obsidian vault.

> [!TIP]
> Start with the **Core Language Foundations**, then follow the map toward data structures, architecture, and real-world applications.


## 🗺️ Map of Content

### 📑 Reference & Cheatsheets

* **Cheatsheets:**
  * [00b - Python Cheatsheet](./00b%20-%20Python%20Cheatsheet.md) — Syntax, primitives, control flow, loops, and core fundamentals.
  * [00c - Python Cheatsheet II](./00c%20-%20Python%20Cheatsheet%20II.md) — Lists, list methods, functions, scope, classes, and modules.


### 🧠 1. Core Language Foundations

* **Variables & Data Types:** [01 - Setup & Data Types](./01%20-%20Setup%20%26%20Data%20Types.md) — Fundamentals, print output, and initial canvas (`str`, `int`, `float`, `bool`).
* **Control Flow Systems:** [02 - Control Flow](./02%20-%20Control%20Flow.md) — Decision-making with `if` / `elif` / `else` and boolean operators (`and`, `or`, `not`).
* **Iterative Logic (Loops):** [03 - Loops](./03%20-%20Loops.md) — Automated iteration with `for` and `while`, control via `break`, `continue`, and `pass`.
* **Projects:** [04 - Terminal Adventure Game](./04%20-%20Terminal%20Adventure%20Game.md) — Interactive CLI control flow project.


### 📦 2. Data Structures (Organization & Storage)

* **Lists (`list`) & Tuples (`tuple`):**
  * [05 - Lists](./05%20-%20Lists.md) — Intro, indexing, slicing, iterating, and core operations.
  * [06 - Built-in Functions & List Methods](./06%20-%20Built-in%20Functions%20%26%20List%20Methods.md) — List methods, bucket list project, and 2D matrices.
* **Dictionaries (`dict`) & Sets (`set`):** Key-value mapping and unique set operations.
* **Comprehensions:** Expressive and efficient single-line creation of lists and dictionaries.


### ⚙️ 3. Modular Architecture (Functions & Modules)

* **Functions:**
  * [07 - Functions](./07%20-%20Functions.md) — The D.R.Y. principle, defining/calling functions, parameters, and arguments.
* **Object-Oriented Programming:**
  * [08 - Object-Oriented Programming](./08%20-%20Object-Oriented%20Programming.md) — Classes, instances, constructors, methods, and OOP principles.
* **Modules & Packages:**
  * [09 - Modules](./09%20-%20Modules.md) — Standard library (`math`, `random`, `datetime`), custom modules, `pip3`, PyPI (`wikipedia`), and The Zen of Python.


```mermaid
flowchart LR
    A[Python Fundamentals] --> B[Data Structures & OOP]
    B --> C[Ecosystem & Modules]
    C --> D[Advanced Core Topics]
