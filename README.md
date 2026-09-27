<div align="center">

# 🧠 Developer Knowledge Base

![Architecture](https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge&logo=structure)
![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7F6DF2?style=for-the-badge&logo=obsidian&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-macOS_M4-000000?style=for-the-badge&logo=apple&logoColor=white)
![Version Control](https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

<p>A structured, multi-language technical repository for computer science foundations, software architecture patterns, and engineering workflows — with every exercise framed around building video games.</p>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />

**Note:**
This knowledge base acts as a central repository for documentation, reference architectures, and code notes authored in **Obsidian** and rendered directly on **GitHub**.

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />



## 🗺️ Knowledge Domains & MOCs

Every domain is self-contained and opens with a **MOC** (Map of Content): an index note
that lists each topic with a one-line description, so you enter through the map instead
of scrolling a folder.

| Domain / Language · Dominio / Lenguaje | Description · Descripción | Notes · Notas | Status · Estado | Map of Content · Mapa de Contenidos |
| :--- | :--- | :--- | :--- | :--- |
| 🐍 **Python** | Core syntax, control flow, data structures, OOP & ecosystems<br>Sintaxis básica, control de flujo, estructuras de datos, POO y ecosistemas | 11 EN · 11 ES | 🟢 Active / Activo | [EN MOC](%F0%9F%90%8D%20Python/README.md)<br>[ES MOC](%F0%9F%90%8D%20Python/README-ES.md) |
| 🚀 **Git & GitHub** | Version control, branching strategies, collaboration & PR workflows<br>Control de versiones, estrategias de ramificación, colaboración y flujos de PR | 4 EN · 4 ES | 🟢 Active / Activo | [EN MOC](%F0%9F%9A%80%20Git%20&%20GitHub/README.md)<br>[ES MOC](%F0%9F%9A%80%20Git%20&%20GitHub/README-ES.md) |
| 🟣 **CSharp** | Strongly typed, OOP, .NET ecosystem & Unity engine architecture<br>Tipado fuerte, POO, ecosistema .NET y arquitectura del motor Unity | 8 EN · 7 ES | 🟢 Active / Activo | [EN MOC](%F0%9F%9F%A3%20CSharp/README.md)<br>[ES MOC](%F0%9F%9F%A3%20CSharp/README-ES.md) |
| 🧮 **Data Structures & Algorithms** | Core data structures, algorithm efficiency & problem solving<br>Estructuras de datos fundamentales, eficiencia de algoritmos y resolución de problemas | 3 EN · 3 ES | 🟢 Active / Activo | [EN MOC](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README.md)<br>[ES MOC](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README-ES.md) |
| ⚙️ **Software Engineering / Ingeniería de Software** | Design patterns, algorithms & system architecture<br>Patrones de diseño, algoritmos y arquitectura de sistemas | — | 🟡 Planned / Planificado | *Coming soon*<br>*Próximamente* |
| 🎮 **Game Architecture / Arquitectura de Juegos** | Interactive mechanics, engine patterns & physics<br>Mecánicas interactivas, patrones de motor y física | — | 🟡 Planned / Planificado | *Coming soon*<br>*Próximamente* |

> The C# domain carries one extra English note: `00b - CSharp Cheatsheet.md` is an empty
> placeholder with no Spanish pair yet, which is why it reads 8 EN · 7 ES.

**Topic numbering.** Notes are prefixed so a domain reads in learning order — `01`, `02`,
`03`… Cheatsheets use a `00b` / `00c` prefix and sit *before* the numbered sequence,
because they are meant to be consulted while working rather than read front to back.

**How to read a note.** Each one is a self-contained lesson: a concept, a runnable
example, its printed output, and the traps worth knowing. Code blocks are executable as
written — the comments state the output you should actually get.

**The Spanish mirror.** Every topic exists in both languages. English is the reference
version; the Spanish note carries a `**Versión original en inglés:**` line at the top
linking back to it. Inside Spanish code blocks, variables and string literals are
localized, while language keywords, API names and class names stay in English.

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />


## 🌍 Languages

| Version · Versión | Entry point · Ruta de entrada | Status · Estado |
| :--- | :--- | :--- |
| 🇬🇧 English (original) · Inglés (original) | [README.md](README.md) | 🟢 Reference base · Base de referencia |
| 🇪🇸 Spanish (translation) · Español (traducción) | [README-ES.md](README-ES.md) | 🟢 In sync · Sincronizado |

Every note exists in both languages. The Spanish note includes a
`**Versión original en inglés:**` line at the top linking back to its English original.
English is the reference version; the Spanish one is kept as a mirror of it.


## 🛠️ Repository Architecture

Notes are stored as **filename pairs** on the same line: the English note first, its
Spanish translation after the `·` separator.

```text
Developer-Knowledge-Base/
├── README.md                              <-- English homepage / Portada en inglés (reference / referencia)
├── README-ES.md                           <-- Spanish homepage / Portada en español (mirror / espejo)
├── LICENSE
├── .gitignore
│
├── 🐍 Python/                             <-- 11 topics / temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - Python Cheatsheet.md         ·  00b - Chuleta de Python.md
│   ├── 00c - Python Cheatsheet II.md      ·  00c - Chuleta de Python II.md
│   ├── 01 - Setup & Data Types.md         ·  01 - Configuración y Tipos de Datos.md
│   ├── 02 - Control Flow.md               ·  02 - Control de Flujo.md
│   ├── 03 - Loops.md                      ·  03 - Bucles.md
│   ├── 04 - Terminal Dungeon Crawl.md     ·  04 - Mazmorra por Terminal.md
│   ├── 05 - Lists.md                      ·  05 - Listas.md
│   ├── 06 - Built-in Functions & List Methods.md  ·  06 - Funciones Integradas y Métodos de Lista.md
│   ├── 07 - Functions.md                  ·  07 - Funciones.md
│   ├── 08 - Object-Oriented Programming.md  ·  08 - Programación Orientada a Objetos.md
│   ├── 09 - Modules.md                    ·  09 - Módulos.md
│   └── z_attachments/                     <-- local assets / recursos locales (empty / vacía, untracked)
│
├── 🚀 Git & GitHub/                       <-- 4 topics / temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction & Setup.md        ·  01 - Introducción y Configuración.md
│   ├── 02 - Core Workflow.md               ·  02 - Flujo de Trabajo Principal.md
│   ├── 03 - Collaboration & Branching.md   ·  03 - Colaboración y Ramas.md
│   └── 04 - Advanced Workflow & PRs.md     ·  04 - Flujo Avanzado y PRs.md
│
├── 🟣 CSharp/                             <-- 7 topics / temas · EN + ES (+ 1 EN-only / solo EN)
│   ├── README.md          ·  README-ES.md
│   ├── 00b - CSharp Cheatsheet.md         <-- empty placeholder / marcador vacío, no ES pair / sin pareja ES
│   ├── 01 - Press Start.md                ·  01 - Pulsa Start.md
│   ├── 02 - Typecast.md                   ·  02 - Conversión de Tipos.md
│   ├── 03 - Control Flow.md               ·  03 - Control de Flujo.md
│   ├── 04 - Loops.md                      ·  04 - Bucles.md
│   ├── 05 - Arrays.md                     ·  05 - Arreglos.md
│   ├── 06 - Methods.md                    ·  06 - Métodos.md
│   └── Mad Dungeon Master - Checkpoint Project.md  ·  Mad Dungeon Master - Proyecto de Hito.md
│
└── 🧮 Data Structures & Algorithms/       <-- 3 topics / temas · EN + ES
    ├── README.md          ·  README-ES.md
    ├── 01 - Introduction to DSA.md        ·  01 - Introducción a Estructuras de Datos y Algoritmos.md
    ├── 02 - Algorithms & Efficiency.md    ·  02 - Algoritmos y Eficiencia.md
    └── 03 - Lists & Linear Search.md      ·  03 - Listas y Búsqueda Lineal.md
```

> The tree above shows the real structure of the repository. Every module ships both a
> `README.md` (English) and a `README-ES.md` (Spanish), and every note exists in both languages.

**Conventions worth knowing / Convenciones que conviene conocer**

| Convention · Convención | Meaning · Significado |
| :--- | :--- |
| `README.md` / `README-ES.md` | The MOC of a domain. Start here.<br>El MOC de un dominio. Empieza por aquí. |
| `NN - Title.md` | A topic note. `NN` encodes the learning order.<br>Una nota de tema. `NN` indica el orden de aprendizaje. |
| `00b` / `00c` | Cheatsheets, consulted on demand.<br>Chuletas, para consultar bajo demanda. |
| `z_attachments/` | Local scratch folder for diagrams. Not versioned.<br>Carpeta local para diagramas. Sin versionar. |
| Pairing · Emparejamiento | Every `.md` has an English original; the Spanish translation sits next to it.<br>Cada `.md` tiene un original en inglés; la traducción va junto a él. |

**Not versioned on purpose / No se versiona a propósito** — listed in `.gitignore` so the
vault stays portable / figura en `.gitignore` para que la vault siga siendo portable:
`.obsidian/` (local vault state / estado local de la vault), `.DS_Store`, and the assistant
tooling folders / y las carpetas de herramientas del asistente `.copilot/`, `.opencode/`,
`copilot/`.


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
```
