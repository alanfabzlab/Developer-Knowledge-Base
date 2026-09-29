
# 03. Día de Mudanza

**Versión original en inglés:** [03 - Moving Day.md](03%20-%20Moving%20Day.md)

**Curso:** Command Line
**Tema:** Cambiar de directorio y listar contenidos
**Tags:** `#cli` `#cd` `#ls` `#navegacion` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Saber dónde estás es la mitad de la navegación. Esta lección cubre la otra mitad: moverse entre directorios y ver qué hay dentro antes de comprometerte a nada.

---

## 1. Moverse con `cd`

`cd` — *change directory* — mueve tu shell a un directorio. Cambia el directorio de trabajo del shell y nada más: no se toca ningún archivo y tu ubicación anterior no queda registrada en ningún sitio.

```bash
$ cd /Users/dev/SunkenKeep
$ cd assets
$ cd sprites
```

Bajar un nivel a la vez, como arriba, es legible pero tedioso. También puedes nombrar la ruta completa de una vez, desde dondequiera que estés:

```bash
$ cd /Users/dev/SunkenKeep/assets/audio
```

Para volver a casa, la tilde es la abreviatura de tu directorio de usuario:

```bash
$ cd ~
```

Y para regresar al lugar de donde venías, `cd -` intercambia al directorio en el que estabas antes del último movimiento:

```bash
$ cd ..
$ cd -
/Users/dev/SunkenKeep/assets
```

> [!WARNING]
> **Trampa**
> `cd` no puede crear nada. Escribir `cd build` en un directorio que no existe informa `no such file or directory` — y la solución es `mkdir build`, que se cubre en [[07 - Recetas]]. Los dos errores comparten el mensaje pero significan lo contrario.

---

## 2. Listar con `ls`

`ls` — *list* — imprime el contenido del directorio actual.

```bash
$ ls
README.md  assets  saves  src
```

Esa única línea es todo el proyecto de un vistazo. El problema es que `ls` a secas no te dice nada sobre las entradas en sí: ni tipo, ni tamaño, ni fecha.

Dos flags lo arreglan:

```bash
$ ls -l
total 24
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src
```

Suma `-a` y aparecen las dos entradas que nadie recuerda:

```bash
$ ls -la
total 32
drwxr-xr-x  6 dev  staff   192 Jan  9 09:14 .
drwxr-xr-x  3 dev  staff    96 Jan  9 09:14 ..
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src
```

| Flag | Muestra |
| :--- | :--- |
| `-l` | Formato largo: permisos, propietario, tamaño, fecha |
| `-a` | Todo, incluidas las entradas que empiezan por `.` |

El primer carácter de cada línea es el tipo: `-` para archivo, `d` para directorio. El `drwxr-xr-x` en `assets` es tu confirmación de que es una carpeta.

> [!WARNING]
> **Trampa**
> `ll` no es `ls -l` en macOS. Algunas distribuciones de Linux lo definen como alias; macOS no, y el shell informa `command not found`. Escribe los flags.

---

## 3. Un flag, varios elementos

`ls` acepta varias rutas a la vez, lo que ahorra un viaje cuando revisas dos ramas del proyecto:

```bash
$ ls -l src saves
saves:
total 16
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 slot-1.dat
-rw-r--r--  1 dev  staff  40 Jan  9 09:14 slot-2.dat

src:
total 16
-rw-r--r--  1 dev  staff  15 Jan  9 09:14 main.gd
-rw-r--r--  1 dev  staff  24 Jan  9 09:14 player.gd
```

Fíjate en que `ls` rotula cada grupo con el nombre de su directorio antes de listar ese grupo. Cuando pasas varias rutas, esas etiquetas son lo que hace la salida legible — un muro de nombres de archivo sin rótulo sería ambiguo.

Esto también funciona con archivos, no solo con directorios — útil para comparar una compilación vieja con la actual:

```bash
$ ls -l src/main.gd saves/slot-1.dat
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 saves/slot-1.dat
-rw-r--r--  1 dev  staff  15 Jan  9 09:14 src/main.gd
```

Cuando todos los argumentos son archivos no hacen falta etiquetas de directorio — las propias rutas dicen cuál es cuál. Fíjate en el orden: `ls` ordena por nombre, así que `saves/` aparece antes que `src/` sin importar el orden en que escribiste los argumentos.

---

## Conclusiones Clave

- `cd` mueve el directorio de trabajo; `cd ~` va a casa y `cd -` vuelve al anterior.
- `cd` nunca crea nada — un directorio ausente significa `mkdir`.
- `ls -l` añade permisos, tamaño y fecha; el `-` o `d` inicial revela archivo frente a directorio.
- `ls -a` revela los archivos ocultos, donde viven `.git` y las configuraciones del editor.
- Varias rutas se pueden listar en una sola llamada a `ls`.

---
