
# 04. Visita a la Casa

**Versión original en inglés:** [04 - House Tour.md](04%20-%20House%20Tour.md)

**Curso:** Command Line
**Tema:** Rutas al directorio padre, rutas absolutas y lectura de archivos con `cat`
**Tags:** `#cli` `#cat` `#relative-paths` `#navegacion` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Aquí termina el Capítulo 1. Ya puedes moverte, puedes mirar, y ahora aprenderás a leer el contenido real de un archivo — la primera vez que el terminal te devuelve algo que no sea un listado de directorios.

---

## 1. Subir con `..`

Desde dentro de `assets/sprites/`, el padre está un `..` más arriba:

```bash
$ cd ..
$ pwd
/Users/dev/SunkenKeep/assets
```

Encadéralos para subir varios niveles en un solo comando. Desde `assets/sprites/`, llegar a la raíz del proyecto toma dos:

```bash
$ cd ../..
$ pwd
/Users/dev/SunkenKeep
```

La regla es mecánica: un `..` por nivel de profundidad. Si estás tres directorios abajo y necesitas la raíz, necesitas tres.

> [!warning] Trampa
> Subir por encima de `/` no es posible. Desde `/`, `cd ..` te deja en `/` y no informa nada — la raíz del sistema de archivos es su propio padre.

---

## 2. Combinar `.` y `..`

Las rutas reales mezclan pasos hacia adelante y subidas. Un único `/` separa cada parte:

```bash
$ cd assets/maps
$ cd ../../saves
$ pwd
/Users/dev/SunkenKeep/saves
```

Aquí la ruta sube dos niveles desde `assets/maps/` y vuelve a bajar a `saves/`. Lee cualquier ruta así de izquierda a derecha como instrucciones y deja de ser un misterio:

> arriba, arriba, baja a `saves/`.

Un `.` suelto significa *quédate en el directorio actual*. Es raro en la práctica, pero aparece en la aritmética de rutas como `./build.sh` — el shell escribe «este directorio» para que la ruta sea inequívocamente relativa.

---

## 3. Leer un archivo con `cat`

`cat` — *concatenate* — imprime el contenido de un archivo en el terminal. Aquí es donde el shell deja de ser un archivador y empieza a ser un lector.

```bash
$ cat saves/slot-1.dat
player: Kaela
level: 02
hp: 78
embers: 340
```

Se pueden imprimir varios archivos uno tras otro, y por eso el comando se llama *concatenate*:

```bash
$ cat saves/slot-1.dat saves/slot-2.dat
player: Kaela
level: 02
hp: 78
embers: 340
player: Roen
level: 05
hp: 41
embers: 1
```

Ambos archivos se imprimen seguidos, sin separador. Eso es precisamente lo que significa *concatenar*, y es la razón por la que `cat` sirve mejor para leer que para combinar — para eso, redirige la salida, como se explica en [[09 - Queso a la Plancha]].

> [!warning] Trampa
> `cat` sobre un directorio informa `Is a directory`. Y sobre un archivo grande —un volcado de assets generado, un log de diez mil líneas— inunda tu terminal sin forma de detenerte a tiempo. `head` muestra solo las primeras líneas, `tail` las últimas, y `less` permite paginar. Recurre a ellos cuando el archivo es grande.

---

## 4. Por qué las rutas necesitan comillas

Cualquier ruta con un espacio debe ir entrecomillada, o el shell la dividirá en argumentos separados y el comando fallará:

```bash
$ cd assets
$ cat "audio files/long-jump.ogg"
```

Las comillas le dicen al shell que tome todo lo que hay entre ellas como un único nombre. Sin ellas, `audio` y `files/long-jump.ogg` se convierten en dos argumentos distintos y `cat` busca un archivo llamado `audio`.

---

## Conclusiones Clave

- `..` sube un nivel; encadénalo para subir varios. `/` es la raíz y su propio padre.
- `.` significa el directorio actual y vuelve explícitas las rutas relativas.
- `cat` imprime el contenido de un archivo y acepta varios a la vez.
- Usa `head`, `tail` o `less` en lugar de `cat` con cualquier cosa grande.
- Las rutas con espacios deben entrecomillarse completas.

---
