
# 09. Queso a la Plancha

**Versión original en inglés:** [09 - Grilled Cheese.md](09%20-%20Grilled%20Cheese.md)

**Curso:** Command Line
**Tema:** Redirección de salida, sobrescribir vs. añadir, combinar con `cat`
**Tags:** `#cli` `#redirection` `#echo` `#streams` `#file-management`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Hasta ahora el shell solo ha *leído* archivos. La redirección lo da vuelta: en lugar de imprimirse en pantalla, la salida de un comando se escribe en un archivo. La diferencia entre una flecha y dos es la diferencia entre empezar de cero y añadir a lo que ya hay.

---

## 1. Sobrescribir con `>`

Un único `>` redirige la salida de un comando a un archivo, **reemplazando su contenido entero**.

```bash
$ mkdir -p design
$ echo "Level 01 - Drowned Gallery" > design/level-notes.txt
$ cat design/level-notes.txt
Level 01 - Drowned Gallery
```

El archivo se crea si no existe. Y si existe, su contenido anterior desaparece:

```bash
$ echo "  - Boss: Guardian of Time" >> design/level-notes.txt
$ echo "  - Loot: Ember Blade" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 01 - Drowned Gallery
  - Boss: Guardian of Time
  - Loot: Ember Blade

$ echo "Level 02 - Collapsed Nave" > design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
```

Tres líneas se convirtieron en una. Nada te avisó.

> ⚠️ **Advertencia:** `>` es incondicional. No hay pregunta, ni copia de seguridad, ni deshacer — el shell no sabe que el contenido anterior importaba. Cualquier comando con `>` puede destruir un archivo, incluidos `cp` y `mv`.

---

## 2. Añadir con `>>`

Dos flechas añaden al final del archivo en lugar de reemplazarlo.

```bash
$ echo "  - Hazard: Drowning" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
```

La primera línea sobrevivió. Esa es toda la diferencia:

| Operador | Archivo existente | Archivo ausente |
| :--- | :--- | :--- |
| `>` | Contenido **reemplazado** | Creado |
| `>>` | Líneas **añadidas** al final | Creado |

> [!warning] Trampa
> Ambos operadores añaden un salto de línea final, y por eso `echo` se combina con ellos limpiamente. Usar `printf` sin `\n` produce un archivo cuya última línea se pega con la siguiente.

---

## 3. Combinar archivos con `cat`

Como la redirección captura la *salida*, funciona con cualquier comando que imprima — incluido el propio `cat`. Eso convierte a `cat` en un concatenador de archivos en disco:

```bash
$ cat design/level-notes.txt saves/slot-1.dat > design/merged.txt
$ cat design/merged.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
player: Kaela
level: 02
hp: 78
embers: 340
```

Cambia el operador para añadir en lugar de reemplazar:

```bash
$ cat saves/slot-2.dat >> design/level-notes.txt
$ cat design/level-notes.txt
Level 02 - Collapsed Nave
  - Hazard: Drowning
player: Roen
level: 05
hp: 41
embers: 1
```

Y con varias fuentes a la vez:

```bash
$ cat saves/slot-1.dat saves/slot-2.dat > design/all-runs.txt
```

> [!warning] Trampa
> Usar `>` con un archivo fuente que es también destino lo trunca antes de la lectura, así que el resultado queda vacío. `cat notes.txt > notes.txt` produce un archivo vacío. La forma segura para reordenar un solo archivo es un nombre temporal, o una append con `>>`.

---

## 4. Construir un archivo de notas

La versión cotidiana de todo lo anterior, donde cada dato es una línea añadida:

```bash
$ mkdir -p design
$ echo "Level 03 - Ember Archive" > design/level-notes.txt
$ echo "  - Boss: Warden of Ash" >> design/level-notes.txt
$ echo "  - Loot: Ember Blade" >> design/level-notes.txt
$ echo "  - Loot: 3 health flasks" >> design/level-notes.txt
$ cat design/level-notes.txt
Level 03 - Ember Archive
  - Boss: Warden of Ash
  - Loot: Ember Blade
  - Loot: 3 health flasks
```

El patrón vale la pena interiorizar: la **primera** escritura usa `>` porque el archivo debe reiniciarse, y cada escritura **posterior** usa `>>` porque debe acumularse. Equivocarte en la primera deja contenido viejo encima de tu entrada nueva; equivocarte en una posterior borra todo lo escrito hasta ese momento.

---

## Conclusiones Clave

- `>` reemplaza el contenido entero de un archivo; `>>` lo añade. Ambos crean el archivo si falta.
- La redirección captura salida, así que funciona con cualquier comando que imprima — `cat` incluido.
- `cat a b > c` concatena archivos en disco; `cat a b >> c` los añade a uno existente.
- Nunca redirijas un archivo hacia sí mismo con `>`; el resultado queda vacío.
- Construye archivos de varias líneas con un `>` seguido de muchos `>>`.

---
