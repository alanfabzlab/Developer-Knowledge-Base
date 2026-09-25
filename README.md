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


| Domain / Language | Description | Status | Map of Content |
| :--- | :--- | :---: | :---: |
| 🐍 **Python** | Core syntax, control flow, data structures, OOP & ecosystems | 🟢 Active | [Go to MOC](./%F0%9F%90%8D%20Python/README.md) |
| 🟣 **C#** | Strongly typed, OOP, .NET ecosystem & Unity engine architecture | 🟢 Active | [Go to MOC](🟣%20CSharp/README.md) |
| 🏗️ **Software Engineering** | Design patterns, algorithms & system architecture | 🟡 Planned | *Coming soon* |
| 🎮 **Game Architecture** | Interactive mechanics, engine patterns & physics | 🟡 Planned | *Coming soon* |

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## 🛠️ Repository Architecture

```text
Developer-Knowledge-Base/
├── 🐍 Python/
│   ├── README.md               <-- Python MOC & topic index
│   └── z_attachments/          <-- Local diagrams & assets
├── 🟣 C#/
│   ├── README.md               <-- C# MOC & topic index
│   ├── 01 - Playing It COOL.md
│   └── z_attachments/          <-- Local diagrams & assets
├── .gitignore                  <-- Git exclusion rules
└── README.md                   <-- Main repository homepage
```


<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## ⚙️ Engineering Workflow

- **Vault Management:** Written and interlinked in [Obsidian](https://obsidian.md).
- **Layout & Rendering:** Designed and formatted using **Visual Studio Code / Trae** + **GitHub Copilot**.
- **Version Control:** Sourced, tracked, and hosted via **Git** & **GitHub**.

```mermaid
gitGraph
   commit id: "Initial commit"
   commit id: "Docs: Obsidian Vault setup"
   branch feature/python
   checkout feature/python
   commit id: "Add Python MOC"
   checkout main
   merge feature/python
   commit id: "Update README structure"
