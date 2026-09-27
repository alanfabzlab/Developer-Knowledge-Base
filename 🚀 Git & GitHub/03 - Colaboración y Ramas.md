

# 03. Colaboración y Ramas

**Versión original en inglés:** [03 - Collaboration & Branching.md](./03%20-%20Collaboration%20&%20Branching.md)

**Curso:** Git & GitHub
**Tema:** Clonado, permisos, fork y gestión de ramas
**Etiquetas:** `#git` `#branching` `#collaboration`



## 1. Clonado del Repositorio y Permisos

Clonar descarga una copia completa de un repositorio remoto de GitHub a tu máquina local[cite: 62].

Bash

```bash
# Clona un repositorio de GitHub
git clone [https://github.com/your-handle/quest-engine.git](https://github.com/your-handle/quest-engine.git)
```


### Niveles de Acceso en GitHub

- **Read:** Permite a los usuarios ver y clonar el repositorio.
    
- **Write:** Permite a los usuarios hacer commit, crear ramas y subir cambios.
    
- **Admin:** Acceso completo a la gestión del repositorio.
    


### Fork

Si no tienes acceso de escritura, el **fork** crea una copia personal del repositorio bajo tu propia cuenta de GitHub para experimentar libremente sin afectar al código original.


## 2. Gestión de Ramas (`git branch` y `git switch`)

Las ramas permiten desarrollo en paralelo sin modificar la línea principal de código (`main`).

Bash

```bash
# Crea una rama nueva
git branch feature/boss-ai

# Cambia a una rama existente
git switch feature/loot-table

# Crea y cambia a una rama nueva en un solo comando
git checkout -b feature/quest-dialogue
```


## 3. Trabajo en Equipo y Sincronización de Cambios (`git pull`)

Cuando trabajas con otras personas, actualiza tu rama local para incorporar los cambios que los miembros del equipo han subido al repositorio remoto.

Bash

```bash
# Obtiene y fusiona los cambios de la rama remota en tu rama local actual
git pull
```

