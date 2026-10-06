
# 02. El Árbol del Proyecto

**Versión original en inglés:** [02 - The Project Tree.md](02%20-%20The%20Project%20Tree.md)

**Curso:** Command Line
**Tema:** Directorios, archivos, rutas y `pwd`
**Tags:** `#cli` `#filesystem` `#paths` `#pwd` `#basics`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Un sistema de archivos es un árbol. Todo lo que guarda la máquina —tu proyecto, un archivo de partida, una tipografía— cuelga de una única raíz. Aprender a leer ese árbol es la habilidad sobre la que se construye el resto del módulo.

---

## 1. Las tres formas

Cada entrada de un sistema de archivos es una de tres cosas:

- **Un archivo** — guarda datos. `player.gd`, `save.dat`, `theme.ogg`.
- **Un directorio** — contiene otras entradas. También llamado *carpeta*; ambas palabras significan lo mismo.
- **Enlace** — un puntero a algo que vive en otro lugar. No necesitaremos esto hasta la gestión de archivos, pero saber que existen evita sorpresas cuando un archivo resulta estar en un sitio distinto al que sugiere su nombre.

Los directorios existen solo para agrupar. `scripts/` y `assets/` contienen el mismo tipo de cosa en un caso y cosas distintas en el otro — la agrupación es una decisión tuya, no una regla que imponga el sistema.

---

## 2. El árbol del proyecto

Este módulo usa un mismo espacio de trabajo en todas las notas: la carpeta de código fuente de un juego 2D llamado **Sunken Keep**.

```text
SunkenKeep/
├── README.md
├── assets/
│   ├── audio/
│   │   ├── door-open.ogg
│   │   └── hit.wav
│   ├── sprites/
│   │   ├── hero.png
│   │   └── lantern.png
│   └── maps/
│       └── level-01.tmx
├── src/
│   ├── main.gd
│   └── player.gd
└── saves/
    ├── slot-1.dat
    └── slot-2.dat
```

Léelo como pares anidados: `assets/` contiene `audio/`, que contiene `door-open.ogg`. Ese es el modelo mental completo — todo lo demás es detalle.

---

## 3. Averiguar dónde estás

`pwd` — *print working directory* — imprime la ruta absoluta del lugar en el que te encuentras.

```bash
$ pwd
/Users/dev/SunkenKeep/assets
```

La salida se divide en tres partes legibles:

| Parte | Valor | Significado |
| :--- | :--- | :--- |
| `/` | raíz | La única entrada de la que parte toda ruta |
| `/Users/dev/SunkenKeep` | home | Tu carpeta de usuario |
| `assets` | actual | Donde estás ahora mismo |

> [!WARNING]
> **Trampa**
> `pwd` no acepta argumentos. Cualquier cosa que le pases se ignora, así que `pwd assets` imprime la misma línea que `pwd` — y si crees que te movió, tu siguiente comando caerá en el directorio equivocado.

---

## 4. Rutas absolutas y relativas

Dos formas de nombrar el mismo lugar, y confundirlas es la fuente más común de «el comando no hizo nada».

**Absoluta** — parte de la raíz. Funciona desde cualquier sitio.

```bash
$ cat /Users/dev/SunkenKeep/saves/slot-1.dat
```

**Relativa** — parte de donde estás. Solo funciona desde aquí.

```bash
$ cat ../saves/slot-1.dat
```

En una ruta relativa, `.` significa *este directorio* y `..` significa *el directorio padre*. El `../` inicial del segundo ejemplo es la forma de subir desde `assets/` hasta `saves/`.

> [!WARNING]
> **Trampa**
> Una ruta relativa se resuelve contra tu **directorio actual**, que cambia en el momento en que haces `cd`. Un comando que funcionaba hace cinco minutos puede estar señalando en silencio a otro sitio. Si dudas, pregunta con `pwd`.

---

## 5. Espacios en los nombres

Las rutas que contienen espacios deben entrecomillarse como un todo, o el shell leerá el espacio como separador y tratará la mitad del nombre como un segundo argumento.

```bash
$ cd "My Game Assets"
```

> [!WARNING]
> **Trampa**
> Esto muerde también en sentido contrario. `cd My Game Assets` falla porque el shell intenta entrar a un directorio llamado `My`. Prefiere `snake_case` o `kebab-case` para los directorios del proyecto y te ahorras el problema — los motores de juegos y el control de versiones también lo prefieren.

---

## Conclusiones Clave

- Un sistema de archivos es un árbol de archivos, directorios y enlaces con raíz en `/`.
- `pwd` imprime tu ubicación absoluta y no acepta argumentos.
- Las rutas absolutas funcionan en cualquier sitio; las relativas dependen de tu directorio actual.
- `..` sube al padre, `.` se queda donde está, y las rutas entrecomilladas manejan los espacios.

---
