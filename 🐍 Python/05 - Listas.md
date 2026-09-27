


<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 05 - Listas

**Versión original en inglés:** [05 - Lists.md](./05%20-%20Lists.md)

**Curso:** Python
**Tema:** Listas de Python, indexación y rebanado, funciones integradas, métodos de lista, iteración sobre listas
**Etiquetas:** `#python` `#lists` `#data-structures` `#arrays` `#fundamentals`


Una **lista** es una colección ordenada de elementos guardada en una sola variable. Las listas se definen usando corchetes `[]` con los elementos separados por comas.

---

## 01. Introducción a las Listas (`boss_stats.py`)

Las listas pueden contener múltiples elementos de datos, valores duplicados y tipos de datos mixtos sin límite de tamaño.

```python
# Storing data using lists
hp_jefe = [980, 870, 920, 960]
daño_ola = [9, 6, 8]
```


### 📝 Ejercicio de Bolsa de Botín (`loot_bag.py`)


```python
# loot_bag.py

bolsa_botin = ['Poción de Salud', 'Espada de Hierro', 'Runa de Bomba', 'Pergamino de Teletransporte', 'Llave Dorada', 'Piel de Monstruo']
print(bolsa_botin)
```


## 02. Indexación, Rebanado y Errores (`quest_log.py`)

### 🔹 Indexación

Los elementos de una lista se acceden mediante su índice de posición basado en cero `[index]`. Los índices negativos cuentan desde el final hacia atrás (`-1` es el último elemento).


```python
elementos = ['Fuego', 'Hielo', 'Rayo', 'Tierra', 'Viento']
# Positive Index: 0, 1, 2, 3, 4
# Negative Index: -5, -4, -3, -2, -1

print(elementos[0])   # Output: Fire
print(elementos[-1])  # Output: Wind
```


### 🔹 Rebanado

El rebanado recupera una subsecuencia de elementos usando `[start:end]`. Incluye el índice `start` y excluye el índice `end`.


```python
elementos = ['Fuego', 'Hielo', 'Rayo', 'Tierra', 'Viento']

print(elementos[0:3]) # Output: ['Fire', 'Ice', 'Lightning']
print(elementos[1:3]) # Output: ['Ice', 'Lightning']
```


### 🔹 IndexError

Un `IndexError` ocurre al intentar acceder a un índice que supera los límites de la secuencia.


```python
# Causes Traceback: IndexError: list index out of range
print(elementos[5]) 
```


### 📝 Ejercicio de Registro de Misiones (`quest_log.py`)


```python
# quest_log.py

registro_misiones = [
  'Derrota al campamento de gobins.',
  'Encuentra la Llave Hundida.',
  'Rescata al comerciante perdido.',
  'Recolecta 10 minerales de hierro.',
  'Prepara un elixir de curación.',
  'Limpia las Minas del Bosque de Cenizas.',
  'Derrota al Golem de Escarcha.',
  'Escapa del templo que se derrumba.'
]

# Print first and second items
print(registro_misiones[0])
print(registro_misiones[1])

# Slice third, fourth, and fifth items
print(registro_misiones[2:5])

# Accessing index 9 causes IndexError
# print(registro_misiones[9])
```



## 03. Funciones Integradas (`inventory.py`)

Python incluye varias funciones integradas diseñadas para trabajar directamente con listas:

* `len()`: Devuelve el número total de elementos de una lista.
* `max()`: Devuelve el valor máximo de una lista.
* `min()`: Devuelve el valor mínimo de una lista.


```python
precios_pociones = [12.50, 9.75, 15.20, 9.75, 18.40, 11.30, 13.60]
precios_runas = [45.10, 32.80, 51.25, 28.40, 39.95, 28.40, 33.60]

print(len(precios_pociones)) # Output: 7
print(max(precios_pociones)) # Output: 18.4
print(min(precios_runas)) # Output: 28.4
```



### 📝 Ejercicio de Rastreador de Botín (`loot_tracker.py`)


```python
# loot_tracker.py

enemigos_derrotados = [452, 318, 197, 806, 645, 274, 903, 261]

# Lowest kill count enemy
print(min(enemigos_derrotados))

# Highest kill count enemy
print(max(enemigos_derrotados))
```


## 04. Métodos de Lista (`spellbook.py`)

Los métodos de lista se llaman usando la notación de punto (`list_name.method()`).

|**Método**|**Descripción**|
|---|---|
|`.append()`|Añade un elemento al final de la lista|
|`.clear()`|Elimina todos los elementos de la lista|
|`.copy()`|Devuelve una copia superficial de la lista|
|`.count()`|Devuelve cuántas veces aparece un valor|
|`.extend()`|Añade otra lista a la lista actual|
|`.index()`|Devuelve el índice de un valor dentro de la lista|
|`.insert()`|Inserta un elemento en una posición especificada|
|`.pop()`|Elimina un elemento de una posición especificada|
|`.remove()`|Elimina el primer elemento con el valor especificado|
|`.reverse()`|Invierte el orden de la lista en el sitio|
|`.sort()`|Ordena la lista en el sitio|



### 🔹 Ejemplo de Uso


```python
codigos_botin = ['SWD', 'SHT', 'BOW', 'POT']

codigos_botin.append('RIN')      # ['SWD', 'SHT', 'BOW', 'POT', 'RIN']
codigos_botin.insert(2, 'HEL')   # ['SWD', 'SHT', 'HEL', 'BOW', 'POT', 'RIN']
codigos_botin.remove('SHT')      # ['SWD', 'HEL', 'BOW', 'POT', 'RIN']
codigos_botin.pop(0)             # ['HEL', 'BOW', 'POT', 'RIN']
```


### 📝 Ejercicio del Libro de Hechizos (`spellbook.py`)


```python
# spellbook.py

libro_hechizos = [
  'Bola de Fuego',
  'Nova de Escarcha',
  'Relámpago en Cadena',
  'Palabra de Cura',
  'Paso Sombrío'
]

libro_hechizos.append('Detención del Tiempo')
libro_hechizos.remove('Palabra de Cura')
libro_hechizos.pop(1)

print(libro_hechizos)
```


## 05. Iteración sobre una Lista (`soundtrack.py`)

### 🔹 Iteración Directa (`for-in`)

Itera directamente sobre los elementos de la lista.


```python
salud_jefe = [320, 280, 410, 190, 540, 260, 130]

for i in salud_jefe:
  print(i)
```


### 🔹 Iteración Basada en Índices (`for-in` con `range()` y `len()`)

Itera a través de los índices usando `range(len(list))`.


```python
salud_jefe = [320, 280, 410, 190, 540, 260, 130]

for i in range(len(salud_jefe)):
  print(salud_jefe[i])
```


### 📝 Ejercicio de Banda Sonora (`soundtrack.py`)


```python
# soundtrack.py

lista_reproduccion = [
  'Obertura de la Carrera de Jefes',
  'Obertura del Reino',
  'Taberna del Ocaso',
  'Cavernas Resonantes',
  'Concierto del Jefe Final',
  'Fanfarria de Victoria'
]

for cancion in lista_reproduccion:
  print(cancion)
```
