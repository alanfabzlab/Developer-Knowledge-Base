

# 🟣 C#: Object-Oriented Foundations & Systems Architecture (MOC)

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%23_12.0-purple?style=for-the-badge&logo=csharp" alt="C#">
  <img src="https://img.shields.io/badge/Ecosystem-.NET_8.0-512BD4?style=for-the-badge&logo=dotnet" alt=".NET">
  <img src="https://img.shields.io/badge/Engine-Unity_Support-black?style=for-the-badge&logo=unity" alt="Unity">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Environment-macOS-lightgrey?style=for-the-badge&logo=apple" alt="macOS">
</p>

> [!NOTE]
> This repository module serves as the central Map of Content (MOC) for C# syntax, object-oriented design patterns, .NET ecosystem fundamentals, and Unity game architecture notes inside this Obsidian vault.

> [!TIP]
> **Learning Roadmap:** Master strong typing and core control structures first, then progress into Object-Oriented Programming (OOP) paradigms, memory management, and real-world game system engineering.

---

## 🗺️ Map of Content

### 📚 Reference & Quick Guides
* **Cheatsheets & Syntax Rules:**
* [00b - CSharp Cheatsheet](./00b%20-%20CSharp%20Cheatsheet.md) — Type system, memory stack vs. heap...

---

### 🧠 1. Core Language Foundations

* **Language Overview:** [01 - Playing It COOL](01%20-%20Playing%20It%20COOL.md) - C# lineage, .NET CLR architecture, compilation pipeline, and top-level statements in Program.cs.
* **Type System & Memory:** [02 - Typecast](02%20-%20Typecast.md) - Value types vs. reference types, explicit/implicit conversion, and string immutability.
* **Control Flow Systems:** [03 - Control Flow](03%20-%20Control%20Flow.md) - Decision making with if/else statements, logical operators (&&, ||, !), and user input evaluation.
* **Iterative Logic & Loops:** [04 - Loops](04%20-%20Loops.md) - Executing repetitive control flow blocks with while/for loops and user-driven exit conditions.
* **Data Collections & Memory:** [05 - Arrays](05%20-%20Arrays.md) - Single-dimensional arrays, indexing, element iteration, and multi-array parallel data processing.
* **Functional Modularity:** [06 - Methods](06%20-%20Methods.md) - Reusable code blocks, parameter passing, return values, and method composition.
* **Checkpoint Project:** [Mad Lyricist - Checkpoint Project](Mad%20Lyricist%20-%20Checkpoint%20Project.md) - Interactive C# lyrics generator applying loops, logic operators, and user input.
---

### 🏗️ 2. Object-Oriented & Software Architecture
* **Encapsulation & Abstraction:** `04 - Classes & Structs` — *Fields, auto-properties, constructors, and stack vs. heap allocation.* `[Planned]`
* **Inheritance & Polymorphism:** `05 - Interfaces & Abstract Classes` — *Virtual methods, overrides, interface implementation, and contract-driven design.* `[Planned]`
* **Advanced Features:** `06 - Generics & LINQ` — *Type-safe data collections, delegates, events, Lambdas, and Language Integrated Query.* `[Planned]`

---

### 🎮 3. Game Development & Engine Integration
* **Unity Lifecycle Scripts:** `07 - MonoBehaviour Architecture` — *`Awake`, `Start`, `Update`, `FixedUpdate` cycles and component linkage.* `[Planned]`
* **Game Systems Design:** `08 - Scriptable Objects & State Machines` — *Data-driven system design, decoupled events, and state-driven game logic.* `[Planned]`

---

<details>
<summary><b>🔍 Quick Access Checklist</b></summary>

- [x] Initial setup & `Program.cs` execution
- [ ] Primitive types & String operations
- [ ] Control flow & Pattern matching
- [ ] OOP Core (Classes, Interfaces, Polymorphism)
- [ ] Unity MonoBehaviour integration
</details>

```mermaid
flowchart LR
    A[C# Core Foundations] --> B[OOP & Architecture]
    B --> C[Unity Engine & Systems]

    click A "#" "Data types, control flow, methods & memory"
    click B "#" "Classes, inheritance, LINQ & interfaces"
    click C "#" "MonoBehaviour lifecycle & ScriptableObjects"
