
# 08. Tipo de Cocina

**Versión original en inglés:** [08 - Cuisine Type.md](08%20-%20Cuisine%20Type.md)

**Curso:** Command Line
**Tema:** Crear archivos con `touch` y extensiones de archivo
**Tags:** `#cli` `#touch` `#archivos` `#extensions` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

`mkdir` construye las carpetas; `touch` crea los archivos que hay dentro. Este es el comando que te permite reservar un nombre antes de que tenga contenido — y la extensión de ese nombre es una decisión que tus herramientas leerán más adelante.

---

## 1. Crear un archivo

`touch` crea un archivo vacío en la ruta indicada.

### Sintaxis

```bash
touch <nombre_archivo>
```

```bash
$ touch saves/slot-3.dat
$ ls -l saves
total 16
-rw-r--r--  1 dev  staff  43 Jan  9 09:14 slot-1.dat
-rw-r--r--  1 dev  staff  40 Jan  9 09:14 slot-2.dat
-rw-r--r--  1 dev  staff   0 Jan  9 09:14 slot-3.dat
```

El tamaño es `0`. El archivo existe, el contenido no — que es exactamente lo que quieres cuando una herramienta se niega a guardar porque falta la ruta de salida.

> **Nota:** Si el archivo ya existe, `touch` actualiza su fecha de modificación y deja intacto el contenido. No puede vaciar un archivo por accidente.

---

## 2. Las extensiones son convención de nombres

El shell trata `hero.png` y `hero` como nombres sin relación. Lo que convierte un archivo en imagen, script o audio es la **extensión** — el texto tras el último punto.

| Extensión | Papel habitual en un proyecto de juego |
| :--- | :--- |
| `.gd` | Script de gameplay |
| `.tscn` | Definición de escena |
| `.tmx` | Datos de mapa de Tiled |
| `.png` | Sprite o imagen de interfaz |
| `.ogg` / `.wav` | Efecto de sonido o música |
| `.dat` | Partida o estado serializado |
| `.json` | Configuración o tabla de datos |
| `.md` | Documentación |

`touch` acepta cualquiera de ellas, porque el shell no interpreta la extensión — lo hacen tu editor, tu motor y el control de versiones.

```bash
$ touch src/enemy.gd src/pickup.gd
$ ls src
enemy.gd  main.gd  pickup.gd  player.gd
```

Varias rutas en un solo comando es el uso normal; no hay razón para ejecutarlo cuatro veces.

---

## 3. Crear en subdirectorios

La ruta puede incluir directorios existentes, que es la forma de dejar un archivo en su sitio sin moverte primero:

```bash
$ touch assets/maps/level-02.tmx
$ ls assets/maps
level-01.tmx  level-02.tmx
```

> **Trampa:** `touch` no crea los directorios intermedios. `touch new-folder/notes.txt` falla con `No such file or directory` si `new-folder` no existe. Crea la carpeta primero con `mkdir -p new-folder`, y luego el archivo.

---

## 4. El hábito que vale la pena

`touch` es más valioso como reserva. Muchas herramientas se niegan a crear su propio directorio y fallan si la ruta no existe, así que precrear la estructura les permite hacer su trabajo:

```bash
$ mkdir -p assets/sfx
$ touch assets/sfx/.gitkeep
$ ls -a assets/sfx
.  ..  .gitkeep
```

El `.gitkeep` vacío mantiene el directorio en el control de versiones, que de otro modo ignora las carpetas sin archivos dentro. La misma razón, otra herramienta: un marcador para algo que debe existir pero aún no tiene nada que decir.

---

## Conclusiones Clave

- `touch` crea un archivo vacío; sobre uno existente solo actualiza la fecha.
- Las extensiones son una convención de nombres que el shell ignora y tu motor lee.
- `touch` acepta varias rutas a la vez y puede apuntar a subdirectorios existentes.
- No crea los directorios padre que falten — usa `mkdir -p` antes.
- Un `.gitkeep` vacío es la forma estándar de mantener un directorio vacío bajo control de versiones.

---
