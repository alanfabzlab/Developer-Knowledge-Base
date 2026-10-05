<div align="center">

# 🧠 Base de Conocimiento para Desarrolladores

![Architecture](https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge&logo=structure)
![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7F6DF2?style=for-the-badge&logo=obsidian&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-macOS_M4-000000?style=for-the-badge&logo=apple&logoColor=white)
![Version Control](https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

<p>Un repositorio técnico estructurado y multilenguaje sobre fundamentos de ciencias de la computación, patrones de arquitectura de software y flujos de trabajo de ingeniería — con cada ejercicio planteado alrededor de la creación de videojuegos.</p>

</div>

**English:** [README.md](README.md)

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />

> **Nota**
> Esta base de conocimiento funciona como un repositorio central de documentación, arquitecturas de referencia y notas de código escritas en **Obsidian** y renderizadas directamente en **GitHub**. Las notas en español son traducciones de las originales en inglés y se mantienen como un espejo: el inglés es la versión de referencia.

## 🗺️ Dominios de Conocimiento y MOCs

Cada dominio es autónomo y abre con un **MOC** (Mapa de Contenidos): una nota índice que
enumera cada tema con una descripción de una línea, para entrar por el mapa en lugar de
recorrer una carpeta.

| Dominio | Descripción | Notas | Estado | Mapa de Contenidos |
| :--- | :--- | :--- | :--- | :--- |
| 🐍 **Python** | Sintaxis básica, control de flujo, estructuras de datos, POO y ecosistemas | 11 EN · 11 ES | 🟢 Activo | [EN](%F0%9F%90%8D%20Python/README.md) · [ES](%F0%9F%90%8D%20Python/README-ES.md) |
| 🚀 **Git & GitHub** | Control de versiones, estrategias de ramificación, colaboración y flujos de PR | 4 EN · 4 ES | 🟢 Activo | [EN](%F0%9F%9A%80%20Git%20&%20GitHub/README.md) · [ES](%F0%9F%9A%80%20Git%20&%20GitHub/README-ES.md) |
| 🟣 **CSharp** | Tipado fuerte, POO, ecosistema .NET y arquitectura del motor Unity | 8 EN · 8 ES | 🟢 Activo | [EN](%F0%9F%9F%A3%20CSharp/README.md) · [ES](%F0%9F%9F%A3%20CSharp/README-ES.md) |
| 🧮 **Estructuras de Datos y Algoritmos** | Estructuras de datos fundamentales, eficiencia de algoritmos y resolución de problemas | 5 EN · 5 ES | 🟢 Activo | [EN](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README.md) · [ES](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README-ES.md) |
| 🖥️ **Línea de Comandos** | Navegación en la terminal, gestión de archivos, permisos y flujo de trabajo en la shell | 13 EN · 13 ES | 🟢 Activo | [EN](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) · [ES](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README-ES.md) |
| 🤖 **GenAI** | Cómo funcionan los LLM, ingeniería de prompts, embeddings y modos de fallo de la IA | 6 EN · 6 ES | 🟢 Activo | [EN](%F0%9F%A4%96%20GenAI/README.md) · [ES](%F0%9F%A4%96%20GenAI/README-ES.md) |
| 🌐 **HTML** | Estructura de páginas web, elementos, atributos, estilos y formularios | 5 EN · 5 ES | 🟢 Activo | [EN](%F0%9F%8C%90%20HTML/README.md) · [ES](%F0%9F%8C%90%20HTML/README-ES.md) |
| 🎨 **CSS** | Estilos, maquetación, responsive y sistemas de diseño | — | 🟡 Planificado | [EN](%F0%9F%8E%A8%20CSS/README.md) · [ES](%F0%9F%8E%A8%20CSS/README-ES.md) |
| ⚙️ **Ingeniería de Software** | Patrones de diseño, algoritmos y arquitectura de sistemas | — | 🟡 Planificado | *Próximamente* |
| 🎮 **Arquitectura de Juegos** | Mecánicas interactivas, patrones de motor y física | — | 🟡 Planificado | *Próximamente* |

**Numeración de los temas.** Las notas llevan un prefijo para que el dominio se lea en orden
de aprendizaje — `01`, `02`, `03`… Las chuletas usan el prefijo `00b` / `00c` y se sitúan
*antes* de la secuencia numerada, porque están pensadas para consultarse mientras se trabaja
y no para leerse de principio a fin.

**El único módulo que se apoya en otro.** 🤖 **GenAI** es la capa de IA de esta vault: parte
del Python de 🐍 **Python** y construye un predictor del siguiente token, una biblioteca de
prompts y un motor de búsqueda semántica en Python puro, de modo que las herramientas de IA
se entiendan por dentro en lugar de pedirlas prestadas a una API.

**Cómo leer una nota.** Cada una es una lección autónoma: un concepto, un ejemplo ejecutable,
su salida por consola y las trampas que conviene conocer. Los bloques de código se ejecutan
tal cual — los comentarios indican la salida que deberías obtener realmente.

**El espejo en español.** Todos los temas existen en ambos idiomas. El inglés es la versión de
referencia; la nota en español incluye una línea `**Versión original en inglés:**` al principio
que enlaza a su original. Dentro de los bloques en español, las variables y las cadenas están
traducidas, mientras que las palabras clave del lenguaje, los nombres de API y los nombres de
clase permanecen en inglés.

## 🌍 Idiomas

| Versión | Ruta de entrada | Estado |
| :--- | :--- | :--- |
| 🇬🇧 Inglés (original) | [README.md](README.md) | 🟢 Base de referencia |
| 🇪🇸 Español (traducción) | [README-ES.md](README-ES.md) | 🟢 Sincronizado |

Cada nota existe en ambos idiomas. Las notas en español incluyen una línea
`**Versión original en inglés:**` en la parte superior que enlaza a su nota original. El inglés
es la versión de referencia y el español se mantiene como su espejo.

## 🛠️ Arquitectura del Repositorio

Las notas se guardan como **pares de nombres de archivo** en la misma línea: primero la nota
en inglés y, tras el separador `·`, su traducción al español.

```text
Developer-Knowledge-Base/
├── README.md                              <-- Portada en inglés (referencia)
├── README-ES.md                           <-- Portada en español (espejo)
├── LICENSE
├── .gitignore
│
├── tools/                                 <-- verificadores de la vault (ver abajo)
├── .github/workflows/                      <-- los ejecuta en cada push
│
├── 🐍 Python/                             <-- 11 temas · EN + ES
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
│   └── z_attachments/                     <-- recursos locales (vacía, sin versionar)
│
├── 🚀 Git & GitHub/                       <-- 4 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction & Setup.md        ·  01 - Introducción y Configuración.md
│   ├── 02 - Core Workflow.md               ·  02 - Flujo de Trabajo Principal.md
│   ├── 03 - Collaboration & Branching.md   ·  03 - Colaboración y Ramas.md
│   └── 04 - Advanced Workflow & PRs.md     ·  04 - Flujo Avanzado y PRs.md
│
├── 🟣 CSharp/                             <-- 8 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - CSharp Cheatsheet.md         ·  00b - Chuleta de CSharp.md
│   ├── 01 - Press Start.md                ·  01 - Pulsa Start.md
│   ├── 02 - Typecast.md                   ·  02 - Conversión de Tipos.md
│   ├── 03 - Control Flow.md               ·  03 - Control de Flujo.md
│   ├── 04 - Loops.md                      ·  04 - Bucles.md
│   ├── 05 - Arrays.md                     ·  05 - Arreglos.md
│   ├── 06 - Methods.md                    ·  06 - Métodos.md
│   └── Mad Dungeon Master - Checkpoint Project.md  ·  Mad Dungeon Master - Proyecto de Hito.md
│
├── 🧮 Data Structures & Algorithms/       <-- 5 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction to DSA.md        ·  01 - Introducción a Estructuras de Datos y Algoritmos.md
│   ├── 02 - Algorithms & Efficiency.md    ·  02 - Algoritmos y Eficiencia.md
│   ├── 03 - Lists & Linear Search.md      ·  03 - Listas y Búsqueda Lineal.md
│   ├── 04 - Binary Search.md              ·  04 - Búsqueda Binaria.md
│   └── 05 - Selection Sort.md             ·  05 - Ordenamiento por Selección.md
│
├── 🖥️ Command Line/                       <-- 13 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - Command Line Cheatsheet.md   ·  00b - Chuleta de Línea de Comandos.md
│   ├── 01 - In The Beginning.md           ·  01 - En los Orígenes.md
│   ├── 02 - Filesystem.md                 ·  02 - Sistema de Archivos.md
│   ├── 03 - Moving Day.md                 ·  03 - Día de Mudanza.md
│   ├── 04 - House Tour.md                 ·  04 - Visita a la Casa.md
│   ├── 05 - Clean Slate.md                ·  05 - Hoja en Blanco.md
│   ├── 06 - Scavenger Hunt.md             ·  06 - Búsqueda del Tesoro.md
│   ├── 07 - Recipes.md                    ·  07 - Recetas.md
│   ├── 08 - Cuisine Type.md               ·  08 - Tipo de Cocina.md
│   ├── 09 - Grilled Cheese.md             ·  09 - Queso a la Plancha.md
│   ├── 10 - Move Around.md                ·  10 - Mover y Renombrar.md
│   ├── 11 - Copy That.md                  ·  11 - Copia Eso.md
│   └── 12 - Music Playlists.md            ·  12 - Listas de Reproducción.md
│
└── 🤖 GenAI/                              <-- 6 temas · EN + ES
    ├── README.md          ·  README-ES.md
    ├── 00b - GenAI Cheatsheet.md          ·  00b - Chuleta de GenAI.md
    ├── 00c - GenAI Cheatsheet II.md       ·  00c - Chuleta de GenAI II.md
    ├── 01 - How AI Thinks.md              ·  01 - Cómo Piensa la IA.md
    ├── 02 - Prompt Engineering.md         ·  02 - Ingeniería de Prompts.md
    ├── 03 - Embeddings & Semantic Search.md  ·  03 - Embeddings y Búsqueda Semántica.md
    ├── 04 - Limits & Risks.md             ·  04 - Límites y Riesgos.md
    └── z_attachments/                     <-- recursos locales (vacía, sin versionar)
```

> El árbol anterior muestra la estructura real del repositorio. Cada módulo incluye su
> `README.md` (inglés) y su `README-ES.md` (español), y cada nota existe en ambos idiomas.

**Convenciones que conviene conocer**

| Convención | Significado |
| :--- | :--- |
| `README.md` / `README-ES.md` | El MOC de un dominio. Empieza por aquí. |
| `NN - Title.md` | Una nota de tema. `NN` indica el orden de aprendizaje. |
| `00b` / `00c` | Chuletas, para consultar bajo demanda. |
| `z_attachments/` | Carpeta local para diagramas. Sin versionar. |
| Emparejamiento | Cada `.md` tiene un original en inglés; la traducción va junto a él. |

**No se versiona a propósito** — figura en `.gitignore` para que la vault siga siendo portable:
`.obsidian/` (estado local de la vault), `.DS_Store` y las carpetas de herramientas del
asistente `.copilot/`, `.opencode/`, `copilot/`.

## ✅ Verificación Automática

La vault se descoloca en silencio: una nota gana una sección, un bloque de código deja de
coincidir con la salida que documenta, el espejo español se queda un paso atrás. Estos
cuatro verificadores lo detectan en cada push, sin que nadie tenga que acordarse de mirar.

| Verificador | Qué demuestra | Corre en |
| :--- | :--- | :--- |
| `.check_readme_index.py` | Que toda nota se alcanza desde algún README; que no hay enlaces rotos; que los totales EN/ES cuadran por módulo. | Linux |
| `tools/check_notes.py` | Que los ``` cierra, que las tablas conservan sus columnas, que los wikilinks resuelven y que las alertas usan los cinco tipos que GitHub dibuja. | Linux |
| `tools/check_parity.py` | Que cada nota tiene su espejo en el otro idioma, con los mismos comandos en el mismo orden. | Linux |
| `tools/check_transcripts.py` | Que cada bloque bash documentado produce de verdad la salida que dice, ejecutándolo contra un árbol de archivos real. | macOS |

```bash
python3 .check_readme_index.py     # índice
python3 tools/check_notes.py       # estructura
python3 tools/check_parity.py      # espejo EN/ES
python3 tools/check_transcripts.py # ejecutar las transcripciones (macOS, zsh)
python3 tools/selftest.py          # comprobar que los verificadores siguen detectando fallos
```

`tools/selftest.py` es el que conviene conocer. Un verificador al que nunca se le ha visto
fallar no demuestra nada: puede estar comprobando la condición equivocada y aun así
informar `OK` para siempre. La autoprueba rompe las notas a propósito en una copia
descartable y falla si algún verificador no se entera.

**Un check en rojo no bloquea nada.** El workflow no es un required status check, así que
un pull request se mergea igual. Es deliberado: escribe esta vault una sola persona, y una
puerta que se interpone a la hora de guardar el trabajo acaba desactivándose. Para cerrarla
más adelante basta una casilla en *Settings → Branches → Branch protection rules*, sin tocar
el workflow: los verificadores ya salen con código distinto de cero cuando algo falla.

Son dos jobs porque los costes son distintos: los tres verificadores de Linux tardan segundos
y cubren toda la vault, mientras que el de transcripciones necesita macOS (zsh y las
herramientas de BSD) y solo cubre los módulos cuyas transcripciones están auditadas. Para
sumar un módulo, añade su carpeta a `MODS` en `tools/check_transcripts.py` y documenta el
árbol de archivos del que parten sus notas.

## ⚙️ Flujo de Trabajo de Ingeniería

- **Gestión de la vault:** escrita y enlazada en [Obsidian](https://obsidian.md).
- **Maquetación y renderizado:** diseñada y formateada con **Visual Studio Code / Trae** + **GitHub Copilot**.
- **Control de versiones:** creado, rastreado y alojado con **Git** y **GitHub**.
- **Traducción:** la versión en español se mantiene como espejo de la inglesa. Las variables, las cadenas y los comentarios se traducen; las palabras clave, los nombres de API y los nombres de clase permanecen en inglés. Los bloques de código se ejecutan con el mismo resultado que sus originales.

```mermaid
gitGraph
   commit id: "Commit inicial"
   commit id: "Vault: Obsidian y estructura"
   branch feature/python
   checkout feature/python
   commit id: "Docs: núcleo de Python y MOC"
   checkout main
   merge feature/python
   branch feature/csharp
   checkout feature/csharp
   commit id: "Docs: arquitectura de C# y Unity"
   checkout main
   merge feature/csharp
   commit id: "Lanzamiento: base v1.0"
```
