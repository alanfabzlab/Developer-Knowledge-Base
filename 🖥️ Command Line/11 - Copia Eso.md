
# 11. Copia Eso

**Versión original en inglés:** [11 - Copy That.md](11%20-%20Copy%20That.md)

**Curso:** Command Line
**Tema:** Duplicar archivos y directorios con `cp` y `cp -r`
**Tags:** `#cli` `#cp` `#backup` `#file-management` `#duplication`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

`mv` reubica; `cp` duplica. La sintaxis es idéntica, y la diferencia es que el original sobrevive. Eso convierte a `cp` en el comando seguro — el que hay que usar cuando una copia de seguridad importa más que un movimiento.

---

## 1. Copiar un archivo

`cp` — *copy* — escribe un duplicado del origen en el destino.

### Sintaxis

```bash
cp <archivo_origen> <archivo_destino>
```

Hacer una copia de respaldo antes de una edición es el uso canónico:

```bash
$ cp design/level-notes.txt design/level-notes.bak
$ ls design
all-runs.txt  level-notes.bak  level-notes.txt  levels  merged.txt
```

Ahora ambos archivos existen, y editar uno no toca el otro.

### Comportamientos Clave

- **Archivo nuevo.** Si el destino no existe, se crea.
- **Archivo existente.** Si ya existe, su contenido es **reemplazado** por el del origen — sin preguntar y sin copia de lo que había.
- **Destino directorio.** Si el destino es un directorio existente, el archivo se copia **dentro** de él con su nombre original.

```bash
$ mkdir -p design/archive
$ cp design/level-notes.txt design/archive/
$ ls design/archive
level-notes.txt
```

> [!WARNING]
> **Trampa**
> El reemplazo es lo que hay que vigilar. `cp importante.txt respaldo.txt` es inofensivo, pero `cp importante.txt importante.txt` trunca el archivo antes de leerlo — la misma trampa de sobrescritura consigo mismo que `cat a > a` en [[09 - Queso a la Plancha|09. Escribiendo el Lore]].

---

## 2. Copiar directorios con `cp -r`

`cp` sobre un directorio informa `is a directory` y no copia nada. El flag `-r` lo hace recursivo, de modo que viene el subárbol completo:

```bash
$ mkdir -p builds/darwin
$ touch builds/darwin/keep
$ cp -r builds/darwin builds/darwin-backup
$ ls builds
darwin  darwin-backup  linux

$ ls -R builds/darwin-backup
keep
```

`ls -R` es el paso de verificación: muestra que la copia contiene realmente lo que contenía el original, que es la única razón para confiar en una copia recursiva.

### Dónde aterriza la copia

Las reglas de destino reflejan las de `mv`, con un añadido:

| Destino | Resultado |
| :--- | :--- |
| Nombre nuevo | La copia se crea con ese nombre |
| Directorio existente | La copia queda **anidada dentro** de él |
| Origen y destino coinciden | Se rechaza: `are identical (not copied)` |

```bash
$ cp -r saves saves-backup
$ ls saves-backup
slot-1.dat  slot-2.dat  slot-3.dat
```

Anidado dentro de una carpeta existente:

```bash
$ mkdir -p backup
$ cp -r saves backup/
$ ls backup
saves
```

> [!WARNING]
> **Trampa**
> Copiar un directorio dentro de otro que ya contiene una copia de él produce `builds/linux and builds/linux are identical (not copied)`. Inofensivo aquí, pero significa que el comando no hizo nada mientras parecía ejecutarse — comprueba dónde acabaron los archivos con `ls` antes de asumir que tienes un respaldo.

---

## 3. Respaldar un directorio

El patrón que conviene conservar: copia antes de tocar nada.

```bash
$ cp -r saves saves-backup
$ rm saves/slot-1.dat
$ ls saves
slot-2.dat  slot-3.dat

$ cp saves-backup/slot-1.dat saves/
$ ls saves
slot-1.dat  slot-2.dat  slot-3.dat
```

`rm` borró el archivo sin confirmación y sin papelera, y la copia lo devolvió. Este es el argumento completo a favor de `cp` en un flujo de trabajo que incluye borrados: el control de versiones protege el código, pero un asset o un archivo de partida fuera del repositorio existe solo donde tú lo pongas.

---

## Conclusiones Clave

- `cp` duplica un archivo dejando el original intacto; `mv` lo reubica.
- Un destino nuevo se crea, un archivo existente se reemplaza, y un directorio existente recibe la copia dentro.
- `cp` sobre un directorio no hace nada sin `-r`.
- `cp -r` sigue las mismas reglas de destino y se niega a copiar un directorio sobre sí mismo.
- Copia antes de borrar — `rm` es irreversible y una copia es el único seguro barato.

---
