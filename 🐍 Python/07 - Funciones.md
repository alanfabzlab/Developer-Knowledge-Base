
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🐍 Funciones en Python y Sintaxis Moderna

![Status Badge](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge&logo=python&logoColor=white)

**Versión original en inglés:** [07 - Functions.md](./07%20-%20Functions.md)

**Curso:** Python
**Tema:** Definición de funciones, parámetros, valores de retorno, ámbito de variables y funciones lambda
**Etiquetas:** `#python` `#programming` `#functions` `#dry` `#open-source` `#notes`


<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />


## 01. El Principio D.R.Y. y las Funciones Integradas (`dry.py`)

Una **función** es un bloque de código reutilizable que realiza una tarea específica. En lugar de repetir bloques de código por todo un programa, puedes envolver el código dentro de una función y ejecutarlo cuando lo necesites.


### 🔹 El Principio D.R.Y.
**D.R.Y.** significa **"No te repitas"**, un principio fundamental del desarrollo de software orientado a reducir la repetición de código y a escribir una lógica limpia y mantenible.


### 🔹 Funciones Integradas
Python incluye 68 funciones integradas listas para usar de inmediato (por ejemplo, `print()`, `input()`, `len()`, `int()`, `type()`).


### 📝 Ejercicio D.R.Y. (`dry.py`)


```python
# dry.py

# print() prints text or values to the console
print('Ready Player One!')

# input() requests user input from the console
hero = input('Enter your hero name: ')

# len() returns the length or number of elements
name_length = len(hero)

# int() converts a value into an integer
level = int('25')

# type() returns the data type of an object
print(type(hero))
```



## 02. Definiendo y Llamando Funciones (`loot_box.py`)

Las funciones definidas por el usuario requieren dos pasos clave:

1. **Definición**: Se crea usando la palabra clave `def`, seguida del nombre de la función, paréntesis `()` y dos puntos `:`. El código interior debe estar indentado.
    
2. **Ejecución (Llamada)**: Se activa escribiendo el nombre de la función seguido de paréntesis `()`.
    


### 📝 Ejercicio del Oráculo de la Caja de Botín (`loot_box.py`)


```python
# loot_box.py
import random

def loot_box():
  random_fortune = random.randint(1, 8)

  if random_fortune == 1:
    print('Don\'t grind for the meta build - invent one.')
  elif random_fortune == 2:
    print('All bosses are hard before they are farmed.')
  elif random_fortune == 3:
    print('The early bird gets the loot, but the second raid gets the legend.')
  elif random_fortune == 4:
    print('Someone in your party needs a health potion from you.')
  elif random_fortune == 5:
    print('Don\'t just think. Press attack!')
  elif random_fortune == 6:
    print('Your heart will skip a beat at 1 HP.')
  elif random_fortune == 7:
    print('The drop you are grinding for is in another chest.')
  else:
    print('Help! I\'m trapped in a cutscene!')


# Function calls
loot_box()
loot_box()
loot_box()
```


## 03. Parámetros y Argumentos

Las funciones se vuelven dinámicas cuando aceptan datos de entrada que procesar.

- **Parámetro**: La variable definida dentro de los paréntesis de la función (el marcador de posición).
    
- **Argumento**: El valor real que se pasa a la función al llamarla.
    


```python
# 'hero' is the parameter
def level_up(hero):
  print('Level up for the hero')
  print('Level up for the hero')
  print('Level up, dear ' + hero)
  print('Level up for the hero')

# 'Aria' is the argument
level_up('Aria')
```



## 04. Valor de Retorno


Una función puede devolver un valor a la línea de código que la llamó usando la palabra clave `return`. 


* **`return`**: Finaliza la ejecución de una función y envía los datos de vuelta al llamador.
* **Retorno Implícito**: Si no se define ninguna sentencia `return`, Python devuelve `None` por defecto.
* **`print()` frente a `return`**: `print()` solo muestra la salida en la terminal, mientras que `return` pasa los datos internamente para que puedan guardarse en variables o procesarse después.


```python
# Exercise 31: Damage Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    return a ** b

# Output execution
print(add(18, 7))        # Output: 25
print(subtract(18, 7))   # Output: 11
print(multiply(18, 7))   # Output: 126
print(divide(18, 6))     # Output: 3.0
print(exp(2, 10))        # Output: 1024
```



## 05. Ámbito de Variables

El ámbito determina en qué parte del programa una variable es visible y accesible.

- **Ámbito Local**: Variables declaradas dentro de una función. Solo existen mientras la función se está ejecutando y no se puede acceder a ellas desde fuera.
    
- **Ámbito Global**: Variables declaradas fuera de cualquier función. Son accesibles en todo el script.
    


```python
# Exercise 32: Damage Log (Time Series Analysis)
damage_per_turn = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.91, 43.87]

def damage_at(x):
    # 'x' is a local variable, 'damage_per_turn' is global
    return damage_per_turn[x - 1]

def max_damage(a, b):
    return max(damage_per_turn[a - 1:b])

def min_damage(a, b):
    return min(damage_per_turn[a - 1:b])

# Tests
print(f"Damage on turn 3: {damage_at(3)}")
print(f"Max damage (turns 1-5): {max_damage(1, 5)}")
print(f"Min damage (turns 5-10): {min_damage(5, 10)}")
```



## 06. Proyecto de Hito: Herrero

Integra funciones, entrada del usuario, estructuras condicionales y valores de retorno en un solo programa.


```python
# Exercise 33: Blacksmith
def welcome():
    print("Welcome to the Blacksmith!")
    print("1. ⚔️ Iron Sword")
    print("2. 🛡️ Leather Shield")
    print("3. 🧪 Health Potion")
    print("4. 🌀 Teleport Scroll")
    print("5. 🔑 Golden Key")

def get_item(x):
    if x == 1:
        return 'Iron Sword'
    elif x == 2:
        return 'Leather Shield'
    elif x == 3:
        return 'Health Potion'
    elif x == 4:
        return 'Teleport Scroll'
    elif x == 5:
        return 'Golden Key'
    else:
        return 'Invalid item'

# Execution flow
welcome()
option = int(input('What would you like to buy? '))
print(f"You bought: {get_item(option)}")
```


---

## 07. Funciones Lambda (Artículo Bonus)

Las funciones lambda (también conocidas como funciones anónimas) son funciones concisas de una sola línea, definidas sin nombre usando la palabra clave `lambda`.

### Sintaxis

```python
lambda arguments: expression
```


- **`lambda`**: Palabra clave usada para definir una función anónima.
    
- **`arguments`**: Entradas que se pasan a la función (separadas por comas).
    
- **`expression`**: Una única expresión que se evalúa y se devuelve automáticamente.
    



### Ejemplo Básico frente a una Función Estándar

**Función Estándar:**


```python
def double_damage(x):
    return x * 2
```


**Equivalente con Lambda:**


```python
double_damage = lambda x: x * 2

print(double_damage(4)) # Output: 8
```


### Casos de Uso Comunes: `map()` y `filter()`

Las funciones lambda destacan cuando se pasan como argumentos de un solo uso a funciones de orden superior como `map()` o `filter()`.


```python
damage_values = [2, 4, 6, 8, 10]

# Using map() to double each element
doubled_damage = list(map(lambda x: x * 2, damage_values))

# Using filter() to keep only the heavy hits
heavy_hits = list(filter(lambda x: x > 7, damage_values))

print(doubled_damage) # Output: [4, 8, 12, 16, 20]
print(heavy_hits)     # Output: [8, 10]
```


### Ejemplos Prácticos

**1. Filtrando Datos de Texto:**


```python
heroes = ['Aria', 'Borin', 'Cass', 'Dara', 'Elowen']

# Filter out hero names starting with 'A'
filtered_heroes = list(filter(lambda name: name[0].upper() != 'A', heroes))

print(filtered_heroes) # Output: ['Borin', 'Cass', 'Dara', 'Elowen']
```


**2. Usando Múltiples Argumentos:**


```python
spell_name = lambda str1, str2: str1 + str2

name = spell_name('fire', 'ball')
print(f'The spell name is: {name}') # Output: The spell name is: fireball
```
