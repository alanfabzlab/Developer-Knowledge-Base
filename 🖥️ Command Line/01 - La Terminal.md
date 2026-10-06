
# 01. La Terminal

**Versión original en inglés:** [01 - The Shell.md](01%20-%20The%20Shell.md)

**Curso:** Command Line
**Tema:** Historial del shell, GUI vs. CLI, primeros comandos
**Tags:** `#cli` `#shell` `#basics` `#terminal` `#game-dev`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Cada sesión de shell empieza igual: abres una ventana y la máquina espera tus instrucciones. Esta primera lección cubre qué es realmente el shell, por qué sobrevive junto a una GUI pulida, y cómo lograr que diga algo en tu primer intento.

---

## 1. Qué es el shell

El **shell** es un programa que lee lo que escribes, lo interpreta y le pide al sistema operativo que lo ejecute. En macOS el predeterminado es **Zsh**; en sistemas más antiguos y en gran parte de Linux encontrarás **Bash**. Ambos hablan la misma gramática, así que todo lo de este módulo funciona en cualquiera de los dos.

La palabra *shell* es literal: escribes un comando, el shell lo expande, se lo entrega al sistema y te devuelve el resultado. No hay nada escondido detrás de un botón.

---

## 2. Por qué la CLI sobrevive a la GUI

Una interfaz gráfica es una capa pintada encima del shell. El shell es la capa que hay debajo, y por eso el terminal sigue ganando en tres situaciones:

- **Repetición.** Diez clics manuales se convierten en un comando que puedes ejecutar cien veces.
- **Precisión.** Un nombre de archivo con un espacio es inequívoco cuando lo entrecomillas.
- **Trabajo remoto.** Un servidor sin escritorio sigue siendo plenamente utilizable.

> [!WARNING]
> **Trampa**
> Una GUI oculta el sistema de archivos. El shell lo muestra. Esa visibilidad es justo el punto — y también la razón por la que un `rm` mal escrito puede ser igual de despiadado que un clic mal puesto.

---

## 3. Tu primer comando

`echo` imprime sus argumentos y nada más. Es la prueba más pequeña de que el shell está escuchando.

```bash
$ echo "Sunken Keep build 0.9.4 compiled"
Sunken Keep build 0.9.4 compiled
```

Sin comillas, el shell separa tu entrada por espacios y `echo` vuelve a unir las partes con espacios simples. La diferencia se hace visible cuando el texto contiene más de un hueco:

```bash
$ echo Level   02 - Flooded Halls
Level 02 - Flooded Halls

$ echo "Level   02 - Flooded Halls"
Level   02 - Flooded Halls
```

> [!WARNING]
> **Trampa**
> Entrecomilla cualquier cosa con **dos espacios seguidos**, una **tabulación** o un **carácter especial** como `*` o `$`. Sin comillas, el shell los expande antes de que `echo` los vea siquiera.

En macOS, `say` lee su argumento en voz alta — realmente útil cuando un log de compilación necesita que tus ojos estén en otra cosa:

```bash
$ say "Level design linked successfully"
```

---

## 4. Leer el prompt

Cada comando que escribes va precedido de un prompt. El predeterminado en los ejemplos de este vault es un `$` simple, que es una convención deliberada para que el prompt nunca compita con la salida:

```text
$ echo "hola"
hola
```

Dos cosas que conviene saber sobre los prompts reales:

- El texto anterior al `$` muestra tu **directorio actual** y tu **rama de git** — un visor de estado gratis.
- El mismo comando escrito dos veces puede mostrar dos prompts distintos y hacer lo mismo. El prompt es decoración; el comando es el trabajo.

---

## 5. Historial del shell

El shell guarda un registro de todo lo que has ejecutado, y las flechas lo recorren.

| Tecla | Acción |
| :--- | :--- |
| `↑` | Comando anterior |
| `↓` | Comando siguiente |
| `Ctrl` + `R` | Buscar en el historial por fragmento |

Pulsa `↑` repetidamente para retroceder hasta encontrar el que quieres, edítalo y ejecútalo. Reescribir una ruta larga es trabajo desperdiciado cuando el shell ya la recuerda por ti.

> [!WARNING]
> **Trampa**
> El historial es por sesión de shell. El comando `history` lo lista, pero una terminal cerrada lo descarta — no hay forma de deshacer entre sesiones un comando que salió mal.

---

## Conclusiones Clave

- El shell interpreta texto y se lo entrega al sistema operativo; la GUI es una capa encima.
- La CLI gana en repetición, precisión y trabajo remoto.
- Entrecomilla siempre el texto que contenga espacios dobles, tabulaciones o metacaracteres del shell.
- Las flechas y `Ctrl + R` convierten tu historial en un registro que se puede buscar.

---
