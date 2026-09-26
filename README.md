<div align="center">

# 🧠 Developer Knowledge Base

![Architecture](https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge&logo=structure)
![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7F6DF2?style=for-the-badge&logo=obsidian&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-macOS_M4-000000?style=for-the-badge&logo=apple&logoColor=white)
![Version Control](https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

<p>A structured, multi-language technical repository for computer science foundations, software architecture patterns, and engineering workflows.</p>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />

> [!NOTE]
> This knowledge base acts as a central repository for documentation, reference architectures, and code notes authored in **Obsidian** and rendered directly on **GitHub**.

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## 🗺️ Knowledge Domains & MOCs

## 🗺️ Knowledge Domains & MOCs

| Domain / Language | Description | Status | Map of Content |
| :--- | :--- | :--- | :--- |
| 🐍 **Python** | Core syntax, control flow, data structures, OOP & ecosystems | 🟢 Active | [Go to MOC](%F0%9F%90%8D%20Python/README.md) |
| 🚀 **Git & GitHub** | Version control, branching strategies, collaboration & PR workflows | 🟢 Active | [Go to MOC](%F0%9F%9A%80%20Git%20%26%20GitHub/README.md) |
| 🟣 **CSharp** | Strongly typed, OOP, .NET ecosystem & Unity engine architecture | 🟢 Active | [Go to MOC](%F0%9F%9F%A3%20CSharp/README.md) |
| 🧮 **Data Structures & Algorithms** | Core data structures, algorithm efficiency & problem solving | 🟢 Active | [Go to MOC](%F0%9F%A7%AE%20Data%20Structures%20%26%20Algorithms/README.md) |
| ⚙️ **Software Engineering** | Design patterns, algorithms & system architecture | 🟡 Planned | *Coming soon* |
| 🎮 **Game Architecture** | Interactive mechanics, engine patterns & physics | 🟡 Planned | *Coming soon* |

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## 🛠️ Repository Architecture

```text
Developer-Knowledge-Base/
├── 🐍 Python/
│   ├── README.md                <-- Python MOC & topic index
│   ├── z_attachments/           <-- Local diagrams & assets
│   └── 01-09_*.md               <-- Topic notes
├── 🚀 Git & GitHub/
│   ├── README.md                <-- Git & GitHub MOC & topic index
│   └── 01-04_*.md               <-- Topic notes
├── 🟣 CSharp/
│   ├── README.md                <-- C# MOC & topic index
│   └── 01-06_*.md               <-- Topic notes
├── 🧮 Data Structures & Algorithms/
│   ├── README.md                <-- DSA MOC & topic index
│   └── 01-03_*.md               <-- Topic notes
├── .gitignore
└── README.md                    <-- Main repository homepage
```


<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## ⚙️ Engineering Workflow

- **Vault Management:** Written and interlinked in [Obsidian](https://obsidian.md).
- **Layout & Rendering:** Designed and formatted using **Visual Studio Code / Trae** + **GitHub Copilot**.
- **Version Control:** Sourced, tracked, and hosted via **Git** & **GitHub**.

```mermaid
gitGraph
   commit id: "Initial commit"
   commit id: "Vault Setup: Obsidian & Structure"
   branch feature/python
   checkout feature/python
   commit id: "Docs: Python Core & MOC"
   checkout main
   merge feature/python
   branch feature/csharp
   checkout feature/csharp
   commit id: "Docs: C# Architecture & Unity"
   checkout main
   merge feature/csharp
   commit id: "Release: Knowledge Base v1.0"
