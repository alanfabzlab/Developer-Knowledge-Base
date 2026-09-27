
# 01. Introducción y Configuración

**Versión original en inglés:** [01 - Introduction & Setup.md](./01%20-%20Introduction%20&%20Setup.md)

**Curso:** Git & GitHub
**Tema:** Descripción general del control de versiones, verificación del entorno y configuración del repositorio
**Etiquetas:** `#git` `#github` `#setup`



## 1. Descripción General e Historia

Git es un sistema de control de versiones distribuido creado por Linus Torvalds en 2005 para gestionar el historial del código fuente del kernel de Linux. GitHub, fundado en 2008, es una plataforma en la nube que aloja repositorios de Git y ofrece herramientas de colaboración.


### Terminología Clave
- **Git:** La herramienta de CLI local que registra los cambios en los archivos a lo largo del tiempo.
- **GitHub:** La plataforma web que aloja repositorios remotos para compartir y colaborar.
- **Repositorio Local:** Una carpeta `.git` almacenada en tu disco local que contiene borradores del historial.
- **Repositorio Remoto:** La copia del proyecto alojada en la nube en GitHub.

---


## 2. Verificación del Entorno

Antes de trabajar con Git, verifica la instalación en la terminal de tu sistema.

Bash

```bash
# Comprueba la versión de Git instalada
git --version
```


_Ejemplo de salida esperada:_ `git version 2.39.3` (o superior).


## 3. Inicialización Local y Enlace con el Remoto

Conectar una carpeta local de un proyecto de videojuegos (por ejemplo, un proyecto de Unity o Godot) a un repositorio de GitHub vacío recién creado implica cuatro pasos fundamentales.


### Paso 1: Inicializar el Repositorio Local

Navega al directorio de tu proyecto e inicializa el seguimiento:

Bash

```bash
# Verifica la ruta del directorio actual
pwd

# Inicializa un repositorio Git vacío
git init
```

Ejecutar `git init` crea un directorio oculto `.git` para almacenar los commits y la configuración local.


### Paso 2: Enlazar con el Repositorio Remoto de GitHub

Adjunta la URL de GitHub como el remoto `origin`:

Bash

```bash
# Añade la conexión al repositorio remoto
git remote add origin [https://github.com/your-handle/quest-engine.git](https://github.com/your-handle/quest-engine.git)
```


### Paso 3: Establecer el Nombre de la Rama por Defecto

Cambia el nombre de la rama por defecto a `main`:

Bash

```bash
# Renombra la rama activa a main
git branch -M main
```


### Paso 4: Verificar la Conexión

Comprueba que la configuración de la rama fue exitosa:

Bash

```bash
# Lista las ramas locales
git branch
```


_Salida esperada:_ `* main`

