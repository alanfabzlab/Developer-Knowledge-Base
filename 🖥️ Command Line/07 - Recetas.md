
# 07. Recetas

**Versión original en inglés:** [07 - Recipes.md](07%20-%20Recipes.md)

**Curso:** Command Line
**Tema:** Crear directorios con `mkdir` y el flag `-p`
**Tags:** `#cli` `#mkdir` `#directorios` `#file-management` `#project-structure`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Los comandos de navegación te dejan explorar una estructura que ya existe. Crearla es otro trabajo: `mkdir` construye las carpetas, y el flag `-p` es lo que separa un comando de un nivel de un árbol entero.

---

## 1. Crear un directorio

`mkdir` — *make directory* — crea una carpeta en la ruta indicada.

### Sintaxis

```bash
mkdir <nombre_directorio>
```

Desde la raíz del proyecto, una carpeta nueva para efectos de sonido:

```bash
$ mkdir assets/sfx
$ ls assets
audio  maps  sfx  sprites
```

La nueva entrada aparece junto a las existentes. El comando no te movió dentro — `mkdir` crea, `cd` entra. Mantenerlos separados es deliberado: a menudo querrás crear varias carpetas antes de entrar en alguna de ellas.

> **Nota:** Crear un directorio no cambia tu directorio de trabajo. Si necesitas trabajar dentro, sigue con `cd` cuando estés listo.

---

## 2. El error habitual

`mkdir` no crea los padres ausentes. Pedir una ruta de dos niveles cuando solo existe el primero falla:

```bash
$ mkdir nope/deeper
mkdir: nope: No such file or directory
```

El mensaje nombra `nope`, no `deeper` — se está quejando del **padre**, que es la parte que no existe. Lee los errores así: nombran lo primero que no pudieron encontrar.

El mismo mensaje aparece por un error distinto. Escribir `cd` donde corresponde `mkdir` produce exactamente la misma redacción:

```bash
$ cd build
cd: no such file or directory: build
```

> [!warning] Trampa
> `no such file or directory` viniendo de `cd` significa que falta la carpeta; viniendo de `mkdir` con una ruta anidada significa que falta el **padre**. Mismas palabras, soluciones opuestas — `mkdir` del padre, o quita la parte anidada.

---

## 3. Rutas anidadas y el flag `-p`

El flag `-p` le indica a `mkdir` que cree todos los niveles ausentes de la ruta, no solo el último. Convierte un proceso de dos pasos en uno:

```bash
$ mkdir builds/linux
mkdir: builds: No such file or directory

$ mkdir -p builds/linux builds/windows
$ ls builds
linux  windows
```

`mkdir -p` tiene dos comportamientos que conviene conocer:

- **Crea los padres que falten.** Los directorios intermedios que ya existen se dejan tal cual, así que el comando es seguro de re-ejecutar.
- **No se queja si el destino ya existe.** A diferencia de `mkdir` a secas, que informa `File exists` y termina con error.

Esa idempotencia es lo que lo convierte en la opción correcta en scripts:

```bash
$ mkdir assets
mkdir: assets: File exists

$ mkdir -p assets
$ echo "exit code: $?"
exit code: 0
```

> [!warning] Trampa
> La indulgencia corta en ambas direcciones. `mkdir -p` construirá encantada una ruta con un error tipográfico, creando `builids/linux` y dejándote preguntándote por qué tu script de compilación ignora la carpeta nueva. El flag no perdona lo *incorrecto*, solo lo *ya existente*.

---

## 4. Construir una matriz de compilaciones

Las compilaciones por plataforma son el caso estándar para la creación anidada — cada plataforma necesita un directorio, y el script no debería importar si ya existen:

```bash
$ mkdir -p builds/linux builds/windows builds/macos builds/web
$ ls builds
linux  macos  web  windows
```

Un comando, cuatro directorios, seguro de ejecutar en cada compilación. Este es el patrón al que hay que recurrir siempre que un árbol de directorios se describa en un script de compilación en lugar de crearse a mano.

---

## 5. Verificar el resultado

Los comandos de creación no informan nada al tener éxito. Confirma la estructura con un listado:

```bash
$ ls -R builds
linux
macos
web
windows

builds/linux:

builds/macos:

builds/web:

builds/windows:
```

`ls -R` lista las entradas de cada directorio y luego desciende a los subdirectorios, etiquetando cada uno con su ruta completa. Es la forma más rápida de comprobar un árbol recién creado — y fíjate en que los cuatro subdirectorios están vacíos, que es justo lo que te está diciendo este listado.

---

## Conclusiones Clave

- `mkdir <nombre>` crea un directorio y no te mueve dentro.
- `mkdir` falla cuando falta el padre — el error nombra al padre, no al destino.
- `mkdir -p` crea todos los niveles ausentes, tolera directorios existentes y es seguro de re-ejecutar.
- `mkdir -p` es la opción correcta en scripts; `mkdir` a secas sirve a mano.
- Verifica un árbol nuevo con `ls -R`.

---
