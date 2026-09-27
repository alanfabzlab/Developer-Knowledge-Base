# 03 - Bucles

**Versión original en inglés:** [03 - Loops.md](./03%20-%20Loops.md)

**Curso:** Python
**Tema:** Sentencias if anidadas, bucles while, bucles for y range(), interpolación de cadenas, tirada de rareza
**Etiquetas:** `#python` `#loops` `#iteration` `#while-loop` `#for-loop` `#logic`

## Bonus: Sentencias if Anidadas

Una **sentencia if anidada** es una sentencia `if` colocada dentro de otra sentencia `if`. La indentación determina el nivel de anidamiento en Python.

### Sintaxis y Lógica Visual

```python
level = 20
gold = 25000

if level >= 18:
  if gold >= 20000:
    print('You are eligible to buy the legendary blade.')
  else:
    print('Your gold is too low for the legendary blade.')
else:
  print('You must reach level 18 to equip legendary gear.')
```


> **Nota:** Evita anidar condiciones a más de 2-3 niveles para mantener la legibilidad del código.
> 



### Ejemplo Práctico: Decisión de Dificultad

```python
difficulty = 'Nightmare'
gear_score = 35

if difficulty == 'Nightmare':
  if gear_score < 60:
    print("You barely survive the dungeon! 💀")
  else:
    print("Even overpowered gear struggles here.")
else:
  print("This difficulty is too easy... let's try a harder one.")
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

print('GATE OF THE SUNKEN KEEP')

passcode = int(input('Enter the passcode: '))

while passcode != 2468:
  passcode = int(input('Incorrect passcode. Enter the passcode again: '))

if passcode == 2468:
  print('Gate unlocked!')
```


## 02. Juego de Adivinar el HP del Jefe (`guess.py`)

Demuestra el control de la ejecución del bucle y la limitación del número total de intentos usando un contador de intentos.

### Lógica Básica de Adivinación


```python
# guess.py (Basic Version)

guess = 0

while guess != 250:
  guess = int(input('Guess the boss HP: '))

print('You got it!')
```



### Juego de Adivinación con Límite de Intentos

Incorporando una variable contadora `tries` junto con operadores lógicos para acotar la ejecución:


```python
# guess.py (Limited Attempts Version)

guess = 0
tries = 0

while guess != 250 and tries < 5:
  guess = int(input('Guess the boss HP: '))
  tries += 1

if guess == 250:
  print('You got it!')
else:
  print('Too many attempts! Better luck next time.')
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
  print('I will not skip the boss cutscene')
```



## 04. Interpolación de Cadenas y Bucles `for` (`99_bosses.py`)

### 🔹 Interpolación de Cadenas (f-strings)

La interpolación de cadenas sustituye valores de variables en marcadores de posición dentro de una cadena usando el prefijo `f` y las llaves `{}`.


```python
# String Interpolation Example
for i in range(5):
  print(f'The damage of {i} is {i*i}')
```



### 🏹 99 Jefes (`99_bosses.py`)

Imprime todos los versos del canto tradicional de mazmorra usando un bucle `for`, `range()` y f-strings:


```python
# 99_bosses.py

for i in range(99, 0, -1):
  print(f'{i} skeletons left in the dungeon')
  print(f'{i} skeletons remain')
  print('Slay one down, and the next spawns')
  print(f'{i-1} skeletons left in the dungeon\n')
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
    print('Legendary')
  elif i % 3 == 0:
    print('Common')
  elif i % 5 == 0:
    print('Rare')
  else:
    print(i)
```
