
# 02. Flujo de Trabajo Principal y Push Local

**Versión original en inglés:** [02 - Core Workflow.md](./02%20-%20Core%20Workflow.md)

**Curso:** Git & GitHub
**Tema:** Directorio de trabajo, área de preparación, commits y push
**Etiquetas:** `#git` `#workflow` `#commits`



## 1. Directorio de Trabajo, Área de Preparación y Repositorio Local

Git clasifica los cambios del espacio de trabajo en tres áreas principales:

- **Directorio de Trabajo:** La carpeta del proyecto en tu computadora. Los cambios aquí son rastreados localmente por Git.
- **Área de Preparación:** Una zona de preparación temporal donde seleccionas cambios específicos antes de guardarlos.
- **Repositorio Local:** El directorio `.git` que contiene las instantáneas confirmadas de tu proyecto.

---


## 2. Preparar Cambios (`git add`)

El comando `git add` mueve los cambios del directorio de trabajo al área de preparación.

Bash

```bash
# Add a single file to staging
git add boss_ai.cs

# Add all changed files in the working directory
git add .

# Add all files matching a specific extension
git add *.cs
```

## 3. Guardar Instantáneas (`git commit`)

Un commit captura una instantánea de los archivos preparados junto con un mensaje explicativo.

Bash

```bash
# Create a commit with a message
git commit -m "feat(combat): agrega tabla de fases de agregacion del jefe"
```

_Buena práctica:_ Mantén los mensajes de commit cortos, claros y descriptivos (por ejemplo, usando Conventional Commits).


## 4. Seguimiento del Estado y Push (`git status` y `git push`)

### Inspeccionar el Estado del Espacio de Trabajo

Bash

```bash
# Check staged, unstaged, and untracked files
git status
```


### Hacer Push al Repositorio Remoto

Bash

```bash
# First time pushing a new branch (sets upstream)
git push -u origin main

# Subsequent pushes
git push
```


## 5. Documentación del Repositorio (`README.md`)

Un archivo `README.md` sirve como documentación principal de un repositorio, explicando qué hace el proyecto, cómo configurarlo y cómo mantenerlo.

