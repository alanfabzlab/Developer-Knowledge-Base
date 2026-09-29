
# 00b. Chuleta de Línea de Comandos

**Versión original en inglés:** [00b - Command Line Cheatsheet.md](00b%20-%20Command%20Line%20Cheatsheet.md)

**Curso:** Command Line
**Tema:** Referencia completa de navegación, gestión de archivos, redirección y atajos
**Tags:** `#cli` `#cheatsheet` `#reference` `#bash` `#terminal`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Referencia de una página para todo el módulo. Los ejemplos usan el árbol del proyecto **Sunken Keep** introducido en [[02 - Sistema de Archivos]].

---

## 🧭 Navegación y Recorrido

| Tarea | Comando | Ejemplo |
| :--- | :--- | :--- |
| **Imprimir directorio actual** | `pwd` | `pwd` |
| **Listar contenidos** | `ls` | `ls` |
| **Listado en formato largo** | `ls -l` | `ls -l` |
| **Incluir entradas ocultas** | `ls -a` | `ls -la` |
| **Listar recursivamente** | `ls -R` | `ls -R content` |
| **Cambiar de directorio** | `cd` | `cd assets` |
| **Subir un nivel** | `cd ..` | `cd ..` |
| **Subir dos niveles** | `cd ../..` | `cd ../..` |
| **Ir a home** | `cd ~` | `cd ~` |
| **Volver al anterior** | `cd -` | `cd -` |
| **Ir a la raíz** | `cd /` | `cd /` |

---

## 📁 Crear Archivos y Directorios

| Tarea | Comando | Ejemplo |
| :--- | :--- | :--- |
| **Crear un directorio** | `mkdir` | `mkdir assets/sfx` |
| **Crear directorios anidados** | `mkdir -p` | `mkdir -p builds/linux builds/win` |
| **Crear un archivo vacío** | `touch` | `touch src/enemy.gd` |
| **Crear varios archivos** | `touch` | `touch src/a.gd src/b.gd` |
| **Mantener un directorio vacío** | `touch` | `touch assets/sfx/.gitkeep` |

---

## ✍️ Texto y Redirección de Salida

| Tarea | Comando | Ejemplo |
| :--- | :--- | :--- |
| **Imprimir texto** | `echo` | `echo "Level 01"` |
| **Sobrescribir archivo con texto** | `echo >` | `echo "Level 01" > notes.txt` |
| **Añadir texto al archivo** | `echo >>` | `echo "  - Boss" >> notes.txt` |
| **Imprimir un archivo** | `cat` | `cat notes.txt` |
| **Sobrescribir archivo con otro** | `cat >` | `cat a.txt > b.txt` |
| **Añadir un archivo a otro** | `cat >>` | `cat a.txt >> b.txt` |
| **Primeras líneas de un archivo** | `head` | `head -5 notes.txt` |
| **Últimas líneas de un archivo** | `tail` | `tail -5 notes.txt` |
| **Paginar un archivo** | `less` | `less notes.txt` |
| **Contar líneas** | `wc -l` | `wc -l notes.txt` |
| **Buscar texto en archivos** | `grep` | `grep -r "Ember" src/` |

---

## 📦 Mover, Copiar y Eliminar

| Tarea | Comando | Ejemplo |
| :--- | :--- | :--- |
| **Mover / renombrar** | `mv` | `mv old-name new-name` |
| **Mover dentro de un directorio** | `mv` | `mv notes.txt design/` |
| **Copiar un archivo** | `cp` | `cp notes.txt notes.bak` |
| **Copiar un directorio** | `cp -r` | `cp -r saves saves-backup` |
| **Eliminar un archivo** | `rm` | `rm notes.txt` |
| **Eliminar un directorio vacío** | `rmdir` | `rmdir tmpdir` |
| **Eliminar un directorio recursivamente** | `rm -r` | `rm -r builds/web` |
| **Confirmar antes de eliminar** | `rm -i` | `rm -i notes.txt` |

> ⚠️ `rm` y `rm -r` son permanentes. Ejecuta `ls` sobre el objetivo primero.

---

## ⌨️ Atajos y Utilidades del Terminal

| Atajo / Utilidad | Acción |
| :--- | :--- |
| **`Tab`** | Autocompleta comandos, archivos y rutas |
| **`Tab` `Tab`** | Lista todas las candidatas para el prefijo |
| **`↑` / `↓`** | Recorre el historial de comandos |
| **`Ctrl` + `R`** | Busca en el historial por fragmento |
| **`Ctrl` + `C`** | Cancela el comando en ejecución |
| **`Ctrl` + `A` / `E`** | Va al principio / final de la línea |
| **`Ctrl` + `L`** | Limpia la pantalla (igual que `clear`) |
| `clear` | Limpia solo la pantalla visible |
| `say "text"` | macOS: lee el texto en voz alta |
| `open .` | macOS: abre el directorio actual en Finder |
| `pbcopy` / `pbpaste` | macOS: copia al / lee del portapapeles |

---

## 🚦 El Orden de las Operaciones

Cuando dudes de qué comando alcanzar:

| Quieres… | Usa |
| :--- | :--- |
| Ver dónde estás | `pwd` |
| Ver qué hay aquí | `ls` |
| Ver el árbol completo | `ls -R` |
| Ir a algún sitio | `cd` |
| Leer un archivo | `cat` (o `less` si es grande) |
| Crear una carpeta | `mkdir -p` |
| Crear un archivo | `touch` |
| Escribir un archivo desde cero | `>` |
| Añadir a un archivo | `>>` |
| Reubicar o renombrar | `mv` |
| Duplicar primero | `cp` |
| Borrar un archivo | `rm` |
| Borrar una carpeta vacía | `rmdir` |
| Borrar una carpeta con contenido | `rm -r` (después de `ls`) |

---

## ⚠️ Las Trampas que Vale la Pena Memorizar

| Error | Qué ocurre |
| :--- | :--- |
| `cd build` cuando no existe | Falla — primero debes `mkdir` |
| `mkdir a/b` cuando falta `a` | Falla — el error nombra al **padre** |
| `mkdir` sobre un directorio existente | Informa `File exists`; usa `-p` |
| `touch carpeta-nueva/archivo.txt` | Falla — `touch` no crea directorios |
| `cat a > a` | Trunca el archivo antes de leerlo — queda vacío |
| `cp a a` | La misma trampa de sobrescritura consigo mismo |
| `echo "x" > notes.txt` dos veces | La segunda llamada borra la primera |
| Ruta con espacios sin comillas | El shell la divide en dos argumentos |
| `rm -r` sin un `ls` antes | Todo lo que está bajo esa ruta desaparece |
| Confiar en `cd -` a ciegas | Alterna entre los dos últimos directorios |
