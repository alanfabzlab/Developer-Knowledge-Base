# 03 - Bucles

**Versión original en inglés:** [03 - Loops.md](./03%20-%20Loops.md)

**Curso:** Python
**Tema:** Sentencias if anidadas, bucles while, bucles for y range(), interpolación de cadenas, tirada de rareza
**Etiquetas:** `#python` `#loops` `#iteration` `#while-loop` `#for-loop` `#logic`

## Bonus: Sentencias if Anidadas

Una **sentencia if anidada** es una sentencia `if` colocada dentro de otra sentencia `if`. La indentación determina el nivel de anidamiento en Python.

### Sintaxis y Lógica Visual

```python
nivel = 20
oro = 25000

if nivel >= 18:
  if oro >= 20000:
    print('Puedes comprar la hoja legendaria.')
  else:
    print('Tu oro es demasiado bajo para la hoja legendaria.')
else:
  print('Debes alcanzar el nivel 18 para equipar equipo legendario.')
```


> **Nota:** Evita anidar condiciones a más de 2-3 niveles para mantener la legibilidad del código.
> 



### Ejemplo Práctico: Decisión de Dificultad

```python
dificultad = 'Pesadilla'
puntuacion_equipo = 35

if dificultad == 'Pesadilla':
  if puntuacion_equipo < 60:
    print("¡Apenas sobrevives a la mazmorra! 💀")
  else:
    print("Incluso el equipo sobredimensionado sufre aquí.")
else:
  print("Esta dificultad es demasiado fácil... probemos una más difícil.")
```



## 01. Introducción a los Bucles y los Bucles `while`

En programación, un **bucle** repite un bloque de código hasta que se cumple una condición específica. Cada repetición de un bucle se llama **iteración**.


### 🔹 El Bucle `while`

Un bucle `while` ejecuta continuamente el código dentro de su bloque mientras su condición se evalúe como `True`.


```python
while condition:
  # code inside executes repeatedly while condition is True
```


### 🏦 Desbloqueo de Archivo de Guardado (`unlock_save.py`)

Simula la verificación de un código de acceso para una puerta de mazmorra bloqueada usando un bucle `while`:


```python
# unlock_save.py

print('PUERTA DE LA FORTALEZA HUNDIDA')

codigo = int(input('Introduce el código de acceso: '))

while codigo != 2468:
  codigo = int(input('Código incorrecto. Introduce el código de nuevo: '))

if codigo == 2468:
  print('¡Puerta desbloqueada!')
```


## 02. Juego de Adivinar el HP del Jefe (`guess.py`)

Demuestra el control de la ejecución del bucle y la limitación del número total de intentos usando un contador de intentos.

### Lógica Básica de Adivinación


```python
# guess.py (Basic Version)

adivina = 0

while adivina != 250:
  adivina = int(input('Adivina el HP del jefe: '))

print('¡Lo has conseguido!')
```



### Juego de Adivinación con Límite de Intentos

Incorporando una variable contadora `tries` junto con operadores lógicos para acotar la ejecución:


```python
# guess.py (Limited Attempts Version)

adivina = 0
intentos = 0

while adivina != 250 and intentos < 5:
  adivina = int(input('Adivina el HP del jefe: '))
  intentos += 1

if adivina == 250:
  print('¡Lo has conseguido!')
else:
  print('¡Demasiados intentos! Mejor suerte la próxima vez.')
```



## 03. Bucles `for` y `range()`

En Python, un **bucle `for`** se usa para iterar sobre una secuencia (como una lista, una tupla o un rango de números). Ejecuta un bloque de código un número determinado de veces cuando se combina con la función `range()`.


### 🔹 La Función `range()`
La función `range()` devuelve una secuencia de números. Por defecto, empieza en `0` y se incrementa en `1`, terminando **un número antes** del límite especificado.


```python
for i in range(6):
  print(i)
```

**Salida:**

```
0
1
2
3
4
5
```

> **Nota:** `range(6)` genera números del `0` al `5` (6 números en total). El límite superior queda excluido.


### 📝 Bucle de Farmeo (`grinding.py`)

Para imprimir un mensaje 100 veces usando un bucle:


```python
# grinding.py

for i in range(100):
  print('No me saltaré la cinemática del jefe')
```



## 04. Interpolación de Cadenas y Bucles `for` (`99_bosses.py`)

### 🔹 Interpolación de Cadenas (f-strings)

La interpolación de cadenas sustituye valores de variables en marcadores de posición dentro de una cadena usando el prefijo `f` y las llaves `{}`.


```python
# String Interpolation Example
for i in range(5):
  print(f'El daño de {i} es {i*i}')
```



### 🏹 99 Jefes (`99_bosses.py`)

Imprime todos los versos del canto tradicional de mazmorra usando un bucle `for`, `range()` y f-strings:


```python
# 99_bosses.py

for i in range(99, 0, -1):
  print(f'{i} esqueletos quedan en la mazmorra')
  print(f'{i} esqueletos quedan')
  print('Mata a uno, y aparece el siguiente')
  print(f'{i-1} esqueletos quedan en la mazmorra\n')
```



## 05. El Reto de la Tirada de Rareza (`rarity_roll.py`)

Un reto clásico que pone a prueba la lógica condicional dentro de una tabla de botín.

### 📋 Reglas del Reto

Itera sobre los números del `1` al `100`:

- Para los múltiplos de **3**, imprime `"Common"`.
    
- Para los múltiplos de **5**, imprime `"Rare"`.
    
- Para los múltiplos de **3 y 5 a la vez**, imprime `"Legendary"`.
    
- Para todos los demás números, imprime el número en sí.
    

### 💡 Implementación


```python
# rarity_roll.py

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('Legendario')
  elif i % 3 == 0:
    print('Común')
  elif i % 5 == 0:
    print('Raro')
  else:
    print(i)
```
