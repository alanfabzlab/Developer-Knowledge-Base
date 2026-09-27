
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

# print() imprime texto o valores en la consola
print('¡Listo Jugador Uno!')

# input() solicita la entrada del usuario desde la consola
heroe = input('Introduce el nombre de tu héroe: ')

# len() devuelve la longitud o el número de elementos
longitud_nombre = len(heroe)

# int() convierte un valor en un entero
nivel = int('25')

# type() devuelve el tipo de dato de un objeto
print(type(heroe))
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
  fortuna_aleatoria = random.randint(1, 8)

  if fortuna_aleatoria == 1:
    print('No farmees por la build meta: inventa una.')
  elif fortuna_aleatoria == 2:
    print('Todos los jefes son difíciles antes de ser farmados.')
  elif fortuna_aleatoria == 3:
    print('El que madruga se lleva el botín, pero la segunda incursión se lleva la leyenda.')
  elif fortuna_aleatoria == 4:
    print('Alguien en tu grupo necesita una poción de salud de tu parte.')
  elif fortuna_aleatoria == 5:
    print('¡Deja de pensar. ¡Pulsa atacar!')
  elif fortuna_aleatoria == 6:
    print('Tu corazón dará un vuelco a 1 HP.')
  elif fortuna_aleatoria == 7:
    print('El objeto por el que farmeas está en otro cofre.')
  else:
    print('¡Ayuda! ¡Estoy atrapado en una cinemática!')


# Llamadas a la función
loot_box()
loot_box()
loot_box()
```


## 03. Parámetros y Argumentos

Las funciones se vuelven dinámicas cuando aceptan datos de entrada que procesar.

- **Parámetro**: La variable definida dentro de los paréntesis de la función (el marcador de posición).
    
- **Argumento**: El valor real que se pasa a la función al llamarla.
    


```python
# 'heroe' es el parámetro
def level_up(heroe):
  print('Sube de nivel el héroe')
  print('Sube de nivel el héroe')
  print('Sube de nivel, querido ' + heroe)
  print('Sube de nivel el héroe')

# 'Aria' es el argumento
level_up('Aria')
```



## 04. Valor de Retorno


Una función puede devolver un valor a la línea de código que la llamó usando la palabra clave `return`. 


* **`return`**: Finaliza la ejecución de una función y envía los datos de vuelta al llamador.
* **Retorno Implícito**: Si no se define ninguna sentencia `return`, Python devuelve `None` por defecto.
* **`print()` frente a `return`**: `print()` solo muestra la salida en la terminal, mientras que `return` pasa los datos internamente para que puedan guardarse en variables o procesarse después.


```python
# Ejercicio 31: Calculadora de Daño
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

# Ejecución de salida
print(add(18, 7))        # Salida: 25
print(subtract(18, 7))   # Salida: 11
print(multiply(18, 7))   # Salida: 126
print(divide(18, 6))     # Salida: 3.0
print(exp(2, 10))        # Salida: 1024
```



## 05. Ámbito de Variables

El ámbito determina en qué parte del programa una variable es visible y accesible.

- **Ámbito Local**: Variables declaradas dentro de una función. Solo existen mientras la función se está ejecutando y no se puede acceder a ellas desde fuera.
    
- **Ámbito Global**: Variables declaradas fuera de cualquier función. Son accesibles en todo el script.
    


```python
# Ejercicio 32: Registro de Daño (Análisis de Series Temporales)
daño_por_turno = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.91, 43.87]

def damage_at(x):
    # 'x' es una variable local, 'daño_por_turno' es global
    return daño_por_turno[x - 1]

def max_damage(a, b):
    return max(daño_por_turno[a - 1:b])

def min_damage(a, b):
    return min(daño_por_turno[a - 1:b])

# Pruebas
print(f"Daño en el turno 3: {damage_at(3)}")
print(f"Daño máximo (turnos 1-5): {max_damage(1, 5)}")
print(f"Daño mínimo (turnos 5-10): {min_damage(5, 10)}")
```



## 06. Proyecto de Hito: Herrero

Integra funciones, entrada del usuario, estructuras condicionales y valores de retorno en un solo programa.


```python
# Ejercicio 33: Herrero
def welcome():
    print("¡Bienvenido al Herrero!")
    print("1. ⚔️ Espada de Hierro")
    print("2. 🛡️ Escudo de Cuero")
    print("3. 🧪 Poción de Salud")
    print("4. 🌀 Pergamino de Teletransporte")
    print("5. 🔑 Llave Dorada")

def get_item(x):
    if x == 1:
        return 'Espada de Hierro'
    elif x == 2:
        return 'Escudo de Cuero'
    elif x == 3:
        return 'Poción de Salud'
    elif x == 4:
        return 'Pergamino de Teletransporte'
    elif x == 5:
        return 'Llave Dorada'
    else:
        return 'Ítem no válido'

# Flujo de ejecución
welcome()
opcion = int(input('¿Qué quieres comprar? '))
print(f"Has comprado: {get_item(opcion)}")
```


---

## 07. Funciones Lambda (Artículo Bonus)

Las funciones lambda (también conocidas como funciones anónimas) son funciones concisas de una sola línea, definidas sin nombre usando la palabra clave `lambda`.

### Sintaxis

```python
lambda argumentos: expresion
```


- **`lambda`**: Palabra clave usada para definir una función anónima.
    
- **`arguments`**: Entradas que se pasan a la función (separadas por comas).
    
- **`expression`**: Una única expresión que se evalúa y se devuelve automáticamente.
    



### Ejemplo Básico frente a una Función Estándar

**Función Estándar:**


```python
def daño_doble(x):
    return x * 2
```


**Equivalente con Lambda:**


```python
daño_doble = lambda x: x * 2

print(daño_doble(4)) # Salida: 8
```


### Casos de Uso Comunes: `map()` y `filter()`

Las funciones lambda destacan cuando se pasan como argumentos de un solo uso a funciones de orden superior como `map()` o `filter()`.


```python
valores_daño = [2, 4, 6, 8, 10]

# Usando map() para duplicar cada elemento
daño_duplicado = list(map(lambda x: x * 2, valores_daño))

# Usando filter() para quedarnos solo con los golpes pesados
golpes_pesados = list(filter(lambda x: x > 7, valores_daño))

print(daño_duplicado) # Salida: [4, 8, 12, 16, 20]
print(golpes_pesados)     # Salida: [8, 10]
```


### Ejemplos Prácticos

**1. Filtrando Datos de Texto:**


```python
lista_heroes = ['Aria', 'Borin', 'Cass', 'Dara', 'Elowen']

# Filtra los nombres de héroes que empiezan por 'A'
heroes_filtrados = list(filter(lambda nombre: nombre[0].upper() != 'A', lista_heroes))

print(heroes_filtrados) # Salida: ['Borin', 'Cass', 'Dara', 'Elowen']
```


**2. Usando Múltiples Argumentos:**


```python
nombre_hechizo = lambda cadena1, cadena2: cadena1 + cadena2

nombre = nombre_hechizo('fuego', 'bola')
print(f'El nombre del hechizo es: {nombre}') # Salida: El nombre del hechizo es: fuegobola
```
