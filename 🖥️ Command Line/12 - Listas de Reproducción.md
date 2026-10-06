
# 12. Construyendo la Mazmorra

**Versión original en inglés:** [12 - Music Playlists.md](12%20-%20Music%20Playlists.md)

**Curso:** Command Line
**Tema:** Repaso del Capítulo 2, listado recursivo y flujo de trabajo completo
**Tags:** `#cli` `#review` `#ls-R` `#workflow` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

El Capítulo 2 trató de cambiar el sistema de archivos: crear, escribir, mover, copiar, borrar. Este ejercicio final reúne todo ello en el flujo de trabajo que realmente ejecutarías al terminar una sesión, y cierra el módulo con `ls -R`, el comando que muestra lo que construiste.

---

## 1. Repaso de comandos del Capítulo 2

| Comando / Flag | Función |
| :--- | :--- |
| `mkdir` | Crea un directorio |
| `mkdir -p` | Crea todos los niveles ausentes; seguro de re-ejecutar |
| `touch` | Crea un archivo vacío; actualiza la fecha si ya existe |
| `echo >` | Escribe texto en un archivo, reemplazando su contenido |
| `echo >>` | Añade una línea a un archivo |
| `cat >` | Escribe el contenido de un archivo en otro, reemplazándolo |
| `cat >>` | Añade el contenido de un archivo a otro |
| `mv` | Mueve o renombra un archivo o directorio |
| `cp` | Copia un archivo |
| `cp -r` | Copia un directorio con su contenido |
| `rm` | Borra un archivo, de forma permanente |
| `rmdir` | Borra un directorio vacío |
| `rm -r` | Borra un directorio y todo lo que hay bajo él |
| `ls -R` | Lista el contenido recursivamente en todos los subdirectorios |

Eso es un kit completo de gestión de archivos: **inspeccionar** con `ls`, **crear** con `mkdir` y `touch`, **escribir** con `>` y `>>`, **reorganizar** con `mv`, **proteger** con `cp`, **eliminar** con `rm` y `rmdir`.

---

## 2. Construir un espacio de nivel

Creando la estructura para un nivel nuevo, con directorios anidados en un solo comando:

```bash
$ mkdir -p content/levels/01-drowned-gallery
$ mkdir -p content/assets/levels/01-drowned-gallery
$ mkdir -p content/scripts/enemies
$ ls -R content
assets
levels
scripts

content/assets:
levels

content/assets/levels:
01-drowned-gallery

content/assets/levels/01-drowned-gallery:

content/levels:
01-drowned-gallery

content/levels/01-drowned-gallery:

content/scripts:
enemies

content/scripts/enemies:
```

Fíjate en el directorio de nivel vacío. `mkdir -p` lo produjo, y por sí solo no sobrevivirá a un commit — el truco de `.gitkeep` de [[08 - Tipo de Cocina|08. Forjando Archivos]] se aplica aquí.

---

## 3. Poblar con notas

Cada escritura posterior a la primera usa `>>`, para que el archivo acumule:

```bash
$ echo "Drowned Gallery" > content/levels/01-drowned-gallery/notes.txt
$ echo "  - Boss: Guardian of Time" >> content/levels/01-drowned-gallery/notes.txt
$ echo "  - Loot: Ember Blade" >> content/levels/01-drowned-gallery/notes.txt
$ echo "  - Enemies: 6 drowned wraiths" >> content/levels/01-drowned-gallery/notes.txt
$ cat content/levels/01-drowned-gallery/notes.txt
Drowned Gallery
  - Boss: Guardian of Time
  - Loot: Ember Blade
  - Enemies: 6 drowned wraiths
```

Añadiendo un script de enemigo por ruta, sin moverte allí primero:

```bash
$ touch content/scripts/enemies/drowned-wraith.gd
$ ls content/scripts/enemies
drowned-wraith.gd
```

---

## 4. Reorganizar y respaldar

La mitad de reorganización de una sesión, en el orden en que realmente la ejecutarías:

```bash
$ cp -r content/levels content/levels-backup
$ mv content/levels/01-drowned-gallery content/levels/02-collapsed-nave
$ mkdir -p content/levels/01-drowned-gallery
$ ls content/levels
01-drowned-gallery  02-collapsed-nave
```

La copia es una red de seguridad para el `mv` que viene después. Cuando el movimiento resulta estar mal, el respaldo ya está ahí.

---

## 5. Verificar el árbol completo

`ls -R` — *recursive list* — recorre todos los subdirectorios e imprime la jerarquía completa:

```bash
$ ls -R content
assets
levels
levels-backup
scripts

content/assets:
levels

content/assets/levels:
01-drowned-gallery

content/assets/levels/01-drowned-gallery:

content/levels:
01-drowned-gallery
02-collapsed-nave

content/levels/01-drowned-gallery:

content/levels/02-collapsed-nave:
notes.txt

content/levels-backup:
01-drowned-gallery

content/levels-backup/01-drowned-gallery:
notes.txt

content/scripts:
enemies

content/scripts/enemies:
drowned-wraith.gd
```

Léelo como un árbol indentado: cada bloque es un directorio, y el prefijo repetido es la ruta completa de su padre. Es lo más parecido que tiene el terminal a un mapa visual de un proyecto.

Fíjate en que el nuevo `01-drowned-gallery` queda vacío — `mv` se llevó su contenido, y el `mkdir -p` de nuevo solo repuso la carpeta. Así es como un nivel suele reiniciarse antes de rehacerse.

> [!WARNING]
> **Trampa**
> `ls -R` no tiene límite de profundidad, así que en un proyecto grande puede imprimir miles de líneas. Añade `| head -50` cuando solo quieras la forma, o `| less` para paginarlo.

---

## 6. Limpiar

Terminar la sesión sin dejar basura:

```bash
$ rmdir content/levels/01-drowned-gallery
$ rm content/levels/02-collapsed-nave/notes.txt
$ rmdir content/levels/02-collapsed-nave
$ rm -r content/levels-backup
$ ls content
assets  levels  scripts
```

Cuatro comandos de borrado para cuatro situaciones distintas: un directorio vacío, un archivo, un directorio que queda vacío una vez borrado el archivo, y un directorio con contenido que ningún comando salvo `rm -r` tocará.

---

## Conclusiones Clave

- El kit del Capítulo 2 es inspeccionar, crear, escribir, reorganizar, proteger, eliminar.
- `mkdir -p` construye árboles anidados; un directorio vacío aún necesita un `.gitkeep` para persistir.
- Usa `>` para la primera escritura de un archivo y `>>` para todas las siguientes.
- Copia antes de mover: `cp -r` primero, `mv` segundo.
- `ls -R` es el paso de verificación; pásalo por `head` en árboles grandes.

---
