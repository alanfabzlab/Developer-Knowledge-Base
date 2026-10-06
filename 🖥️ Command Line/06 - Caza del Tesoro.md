
# 06. Caza del Tesoro

**Versión original en inglés:** [06 - Treasure Hunt.md](06%20-%20Treasure%20Hunt.md)

**Curso:** Command Line
**Tema:** Repaso del Capítulo 1 y reto de navegación
**Tags:** `#cli` `#review` `#challenge` `#navegacion` `#filesystem`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

El Capítulo 1 es navegación: saber dónde estás, moverte, mirar y leer. Este es un punto de control — una búsqueda del tesoro por el proyecto que usa todos los comandos de las primeras cinco lecciones, en el orden en que realmente los usarías.

---

## 1. Resumen de comandos del Capítulo 1

| Comando | Sintaxis | Descripción |
| :--- | :--- | :--- |
| `echo` | `echo [texto]` | Imprime texto en la salida estándar |
| `pwd` | `pwd` | Imprime la ruta absoluta del directorio de trabajo |
| `ls` | `ls [ruta]` | Lista las entradas de un directorio |
| `ls -l` | `ls -l [ruta]` | Formato largo: permisos, propietario, tamaño, fecha |
| `ls -a` | `ls -a [ruta]` | Incluye entradas cuyo nombre empieza por `.` |
| `cd` | `cd [directorio]` | Entra en un directorio |
| `cd ..` | `cd ..` | Sube al directorio padre |
| `cd ~` | `cd ~` | Va a tu directorio home |
| `cd -` | `cd -` | Regresa al directorio anterior |
| `cat` | `cat [archivo]` | Imprime el contenido de un archivo |
| `clear` | `clear` | Limpia la pantalla visible |
| `Tab` | `Tab` | Completa un comando o una ruta |

---

## 2. Las pistas

Trabaja desde la raíz del proyecto y responde cada una usando el comando que corresponda. Si un paso necesita más de lo que has aprendido, esa es la pista de que te saltaste algo.

1. ¿Dónde estoy exactamente? Imprime la ruta completa.
2. ¿Qué hay en el nivel superior del proyecto? Listalo.
3. ¿Cuáles de esos son directorios y no archivos? Muestra tipo, tamaño y fecha.
4. ¿Hay algo aquí cuyo nombre empiece por un punto? Incluye las entradas ocultas.
5. ¿A qué directorio me muevo para llegar a los sprites?
6. ¿Cómo llego al directorio padre del directorio en el que estoy?
7. ¿Cómo regreso al directorio en el que estaba antes de eso?
8. Imprime el contenido del primer archivo de partida sin abrir un editor.
9. Imprime los dos archivos de partida uno tras otro.
10. ¿Qué hay en el directorio de mapas?
11. Limpia la pantalla sin perder mi ubicación. ¿Dónde estoy después?
12. Completa `cd SunkenKeep/assets/a` hasta un nombre de directorio completo usando una sola tecla.

---

## 3. Un recorrido

Una ruta a través de la búsqueda, con la salida que produce cada paso:

```bash
$ pwd
/Users/dev/SunkenKeep

$ ls
README.md  assets  saves  src

$ ls -l
total 24
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src

$ ls -la
total 32
drwxr-xr-x  6 dev  staff   192 Jan  9 09:14 .
drwxr-xr-x  3 dev  staff    96 Jan  9 09:14 ..
-rw-r--r--  1 dev  staff    37 Jan  9 09:14 README.md
drwxr-xr-x  5 dev  staff   160 Jan  9 09:14 assets
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 saves
drwxr-xr-x  4 dev  staff   128 Jan  9 09:14 src

$ cd assets/sprites
$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ cd ..
$ pwd
/Users/dev/SunkenKeep/assets

$ cd -
/Users/dev/SunkenKeep/assets/sprites

$ cat ../../saves/slot-1.dat
player: Kaela
level: 02
hp: 78
embers: 340

$ cat ../../saves/slot-1.dat ../../saves/slot-2.dat
player: Kaela
level: 02
hp: 78
embers: 340
player: Roen
level: 05
hp: 41
embers: 1

$ ls ../maps
level-01.tmx

$ clear

$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ cd SunkenKeep/assets/a<Tab>
cd: no such file or directory

$ pwd
/Users/dev/SunkenKeep/assets/sprites
```

Ese último paso merece una pausa: `Tab` completó el nombre perfectamente y el comando aun así falló, porque el terminal ya estaba dentro de `SunkenKeep`. Una ruta relativa solo se resuelve desde donde estás — la regla de [[02 - El Árbol del Proyecto]] apareciendo exactamente donde suele morder.

El segundo `pwd` es justamente lo que busca la pista. Un `cd` fallido te deja exactamente donde estabas, y por eso conviene adquirir el hábito de comprobar tu ubicación después de un error.

> [!WARNING]
> **Trampa**
> `cd -` alterna entre los dos últimos directorios, así que ejecutarlo dos veces te devuelve al punto de partida. También es la forma más fácil de acabar donde no querías, porque anula cualquier `cd` que tenías intención de hacer.

---

## Conclusiones Clave

- El Capítulo 1 te dio seis verbos: `pwd` para ubicarte, `ls` para mirar, `cd` para moverte, `cat` para leer, `clear` para reiniciar la vista y `Tab` para escribir menos.
- `cd -` alterna entre los dos últimos directorios y anulará un `cd` previsto.
- Las rutas relativas se resuelven contra el directorio actual, que cambia con cada `cd`.
- Imprime un listado siempre antes de borrar algo — ese hábito empieza en este capítulo.

---
