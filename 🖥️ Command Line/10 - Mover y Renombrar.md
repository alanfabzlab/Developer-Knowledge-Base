
# 10. Mover y Renombrar

**Versión original en inglés:** [10 - Move Around.md](10%20-%20Move%20Around.md)

**Curso:** Command Line
**Tema:** Mover, renombrar y borrar con `mv`, `rm` y `rmdir`
**Tags:** `#cli` `#mv` `#rm` `#rmdir` `#file-management` `#deletion`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Esta es la lección con los bordes más afilados del módulo. `mv` es el comando más útil de aquí y `rm` el más peligroso; ambos tienen la misma forma de dos argumentos, y saber cómo se interpreta el segundo es lo que los distingue.

---

## 1. Mover con `mv`

`mv` — *move* — reubica un archivo o directorio.

### Sintaxis

```bash
mv <origen> <destino>
```

Los dos destinos se comportan de forma distinta, y esa diferencia es la clave de todo el comando.

**Hacia un directorio existente** — el archivo entra y conserva su nombre:

```bash
$ echo "Level 05 - Ashen Spire" > design/boss-notes.txt
$ mv design/boss-notes.txt assets/audio/
$ ls assets/audio
boss-notes.txt  door-open.ogg  hit.wav
```

**Hacia un nombre nuevo** — el elemento se renombra en su sitio:

```bash
$ mv assets/audio/boss-notes.txt assets/audio/boss-tips.txt
$ ls assets/audio
boss-tips.txt  door-open.ogg  hit.wav
```

La segunda vez no se movió nada. La única diferencia entre ambas llamadas es si el destino ya existe como directorio.

Los directorios se mueven igual, con todo su contenido:

```bash
$ mv builds/macos builds/darwin
$ ls builds
darwin  linux  web  windows
```

> **Trampa:** Un destino directorio que no existe se trata como un **nombre nuevo**, no como una ubicación. `mv saves saved` renombra la carpeta; `mv saves archive/` falla salvo que `archive/` ya exista. Créala antes con `mkdir -p archive`.

---

## 2. Borrar archivos con `rm`

`rm` — *remove* — borra archivos de forma permanente, inmediata y sin confirmación.

```bash
$ mkdir -p design/levels
$ touch design/scratch.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt  scratch.txt

$ rm design/scratch.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt
```

Varios de una vez:

```bash
$ touch design/a.txt design/b.txt
$ rm design/a.txt design/b.txt
$ ls design
all-runs.txt  level-notes.txt  levels  merged.txt
```

No hay un `-i` que pregunte por defecto, ni carpeta de papelera. El archivo se acabó.

> ⚠️ **Advertencia:** `rm` evita por completo la papelera del sistema. No hay deshacer, ni confirmación, ni segunda oportunidad — una ruta mal escrita borra el archivo equivocado, y un flag mal escrito puede borrar mucho más de lo previsto. Haz siempre `ls` del objetivo justo antes de borrarlo.

---

## 3. Borrar directorios con `rmdir`

`rmdir` elimina un directorio, pero **solo si está vacío**. Esa restricción es una medida de seguridad, y es la razón para preferirlo sobre `rm -r` en la limpieza de rutina.

```bash
$ mkdir -p tmpdir
$ rmdir tmpdir
```

Varios a la vez, útil para limpiar una tanda de directorios de compilación vacíos:

```bash
$ mkdir -p x1 x2 x3
$ rmdir x1 x2 x3
$ echo "exit code: $?"
exit code: 0
```

Frente a un directorio con contenido, se niega:

```bash
$ rmdir design
rmdir: design: Directory not empty
```

Esa negativa es el objetivo. No puedes borrar por accidente una carpeta de proyecto poblada con `rmdir`, porque el comando ni lo intenta.

---

## 4. Borrado recursivo con `rm -r`

Cuando un directorio está genuinamente vacío de nada, `-r` lo elimina junto con cada archivo y subdirectorio que contiene.

```bash
$ rm -r builds/web
$ ls builds
darwin  linux  windows
```

> ⚠️ **Advertencia:** `rm -r` es el comando que hay que escribir con cuidado y nunca pegar de una fuente sin verificar. El flag recursivo elimina *todo* lo que está bajo el objetivo, sin preguntar. Confirma la ruta con `pwd` e inspéchala con `ls` antes — los dos segundos que cuesta son la diferencia entre una limpieza y una tarde perdida.

El hábito que lo hace seguro: navegar al padre y listar antes de borrar.

```bash
$ cd builds
$ ls
darwin  linux  windows
$ rm -r windows
$ ls
darwin  linux
```

---

## Conclusiones Clave

- `mv origen destino` mueve dentro de un directorio si existe, y renombra si no.
- `rm` borra archivos de forma permanente, sin pregunta y sin papelera.
- `rmdir` borra solo directorios vacíos — su negativa es una medida de seguridad.
- `rm -r` elimina un directorio y todo lo que hay bajo él; verifica la ruta antes de ejecutarlo.
- Lista el objetivo inmediatamente antes de cualquier borrado.

---
