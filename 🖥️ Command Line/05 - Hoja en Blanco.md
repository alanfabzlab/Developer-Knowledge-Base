
# 05. Hoja en Blanco

**Versión original en inglés:** [05 - Clean Slate.md](05%20-%20Clean%20Slate.md)

**Curso:** Command Line
**Tema:** Limpiar la pantalla, historial de comandos y autocompletado con Tab
**Tags:** `#cli` `#clear` `#history` `#tab-completion` `#productividad`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Una sesión larga llena el terminal de salida hasta que el comando que te importa queda en algún punto del medio. Esta lección trata de mantener la pantalla legible y las manos lejos del teclado.

---

## 1. Limpiar la pantalla

`clear` borra el texto visible y te deja un prompt limpio arriba.

```bash
$ clear
```

Ese es el comando completo. No acepta argumentos ni hace nada con tus archivos.

> **Importante:** `clear` solo redibuja lo que ves. **No** te mueve, **no** borra nada y **no** reinicia las variables de entorno. Tu directorio de trabajo es exactamente el de antes.

Para demostrarlo, limpia desde lo más profundo del proyecto y comprueba inmediatamente después:

```bash
$ pwd
/Users/dev/SunkenKeep/assets/sprites

$ clear

$ pwd
/Users/dev/SunkenKeep/assets/sprites
```

La pantalla está en blanco, la ubicación no cambió. Un terminal vacío es un reinicio cosmético, no una sesión nueva.

---

## 2. Historial de comandos

El shell registra cada comando que ejecutas en la sesión actual. Las flechas recorren ese registro.

| Tecla | Acción |
| :--- | :--- |
| `↑` | Volver al comando anterior |
| `↓` | Avanzar al comando siguiente |

Pulsa `↑` repetidamente para retroceder, detente en el comando que quieras y edítalo antes de ejecutarlo. Reescribir una ruta larga desperdicia un esfuerzo que el shell ya gastó en recordarla.

### Buscar en lugar de desplazarse

Cuando el registro es largo, `Ctrl + R` es más rápido que las flechas. Escribe un fragmento y el shell busca en tu historial la primera coincidencia:

```text
$ Ctrl + R, y luego escribe "slot"
(reverse-i-search)`slot': cat saves/slot-1.dat
```

Pulsa `Enter` para ejecutarlo, o `Ctrl + R` otra vez para buscar la siguiente coincidencia.

> **Trampa:** El historial es por sesión. Cierra el terminal y el registro desaparece — no hay forma de recuperar un comando de una sesión que ya terminó.

---

## 3. Autocompletado con Tab

La tecla `Tab` completa lo que llevas escrito. Púlsala una vez y el shell rellena el resto; púlsala dos veces y te lista todas las opciones que comparten tu prefijo.

Completando un nombre de directorio:

```text
$ cd Sun<Tab>
$ cd SunkenKeep/

$ cd SunkenKeep/src/<Tab><Tab>
config/  player.gd  main.gd
```

Ese segundo ejemplo es el útil: dos pulsaciones te muestran todas las opciones en lugar de adivinar, y así es como descubres un directorio `config/` que habías olvidado que existía.

El autocompletado funciona con nombres de comandos, archivos y rutas de directorios — lo que convierte las rutas largas del proyecto en un asunto de dos teclas.

> **Trampa:** Si no se completa nada, no hay coincidencia para lo que escribiste. La causa más común es estar en el directorio equivocado; una ruta que resuelve desde otro sitio se ve igual aquí. Confírmalo con `pwd`.

---

## 4. Un atajo que vale la pena interiorizar

Una sesión de tres pasos, hecha rápida:

```bash
$ cd Sun<Tab>
$ ls -la as<Tab><Tab>
$ cat assets/maps/level-01.tmx
```

Las dos primeras líneas cuestan cuatro pulsaciones. Escribirlas a mano cuesta unas cuarenta. Este es el pago de todo el capítulo: el terminal no es más rápido porque se escriba rápido, sino porque el shell termina tus frases por ti.

---

## Conclusiones Clave

- `clear` borra solo la pantalla visible — ubicación, archivos y variables quedan intactos.
- `↑` y `↓` recorren el historial de la sesión; `Ctrl + R` lo busca.
- `Tab` completa comandos y rutas; `Tab` dos veces lista todas las candidatas.
- El historial no sobrevive a la sesión, así que captura lo que necesites antes de cerrar.

---
