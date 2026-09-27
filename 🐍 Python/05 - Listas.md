


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
boss_hp = [980, 870, 920, 960]
wave_damage = [9, 6, 8]
```


### 📝 Ejercicio de Bolsa de Botín (`loot_bag.py`)


```python
# loot_bag.py

loot_bag = ['Health Potion', 'Iron Sword', 'Bomb Rune', 'Teleport Scroll', 'Golden Key', 'Monster Pelt']
print(loot_bag)
```


## 02. Indexación, Rebanado y Errores (`quest_log.py`)

### 🔹 Indexación

Los elementos de una lista se acceden mediante su índice de posición basado en cero `[index]`. Los índices negativos cuentan desde el final hacia atrás (`-1` es el último elemento).


```python
elements = ['Fire', 'Ice', 'Lightning', 'Earth', 'Wind']
# Positive Index: 0, 1, 2, 3, 4
# Negative Index: -5, -4, -3, -2, -1

print(elements[0])   # Output: Fire
print(elements[-1])  # Output: Wind
```


### 🔹 Rebanado

El rebanado recupera una subsecuencia de elementos usando `[start:end]`. Incluye el índice `start` y excluye el índice `end`.


```python
elements = ['Fire', 'Ice', 'Lightning', 'Earth', 'Wind']

print(elements[0:3]) # Output: ['Fire', 'Ice', 'Lightning']
print(elements[1:3]) # Output: ['Ice', 'Lightning']
```


### 🔹 IndexError

Un `IndexError` ocurre al intentar acceder a un índice que supera los límites de la secuencia.


```python
# Causes Traceback: IndexError: list index out of range
print(elements[5]) 
```


### 📝 Ejercicio de Registro de Misiones (`quest_log.py`)


```python
# quest_log.py

quest_log = [
  'Defeat the goblin camp.',
  'Find the Sunken Key.',
  'Rescue the lost merchant.',
  'Collect 10 iron ore.',
  'Brew a healing elixir.',
  'Clear the Ashwood Mines.',
  'Defeat the Frost Golem.',
  'Escape the collapsing temple.'
]

# Print first and second items
print(quest_log[0])
print(quest_log[1])

# Slice third, fourth, and fifth items
print(quest_log[2:5])

# Accessing index 9 causes IndexError
# print(quest_log[9])
```



## 03. Funciones Integradas (`inventory.py`)

Python incluye varias funciones integradas diseñadas para trabajar directamente con listas:

* `len()`: Devuelve el número total de elementos de una lista.
* `max()`: Devuelve el valor máximo de una lista.
* `min()`: Devuelve el valor mínimo de una lista.


```python
potion_prices = [12.50, 9.75, 15.20, 9.75, 18.40, 11.30, 13.60]
rune_prices = [45.10, 32.80, 51.25, 28.40, 39.95, 28.40, 33.60]

print(len(potion_prices)) # Output: 7
print(max(potion_prices)) # Output: 18.4
print(min(rune_prices)) # Output: 28.4
```



### 📝 Ejercicio de Rastreador de Botín (`loot_tracker.py`)


```python
# loot_tracker.py

enemy_kills = [452, 318, 197, 806, 645, 274, 903, 261]

# Lowest kill count enemy
print(min(enemy_kills))

# Highest kill count enemy
print(max(enemy_kills))
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
loot_codes = ['SWD', 'SHT', 'BOW', 'POT']

loot_codes.append('RIN')      # ['SWD', 'SHT', 'BOW', 'POT', 'RIN']
loot_codes.insert(2, 'HEL')   # ['SWD', 'SHT', 'HEL', 'BOW', 'POT', 'RIN']
loot_codes.remove('SHT')      # ['SWD', 'HEL', 'BOW', 'POT', 'RIN']
loot_codes.pop(0)             # ['HEL', 'BOW', 'POT', 'RIN']
```


### 📝 Ejercicio del Libro de Hechizos (`spellbook.py`)


```python
# spellbook.py

spellbook = [
  'Fireball',
  'Frost Nova',
  'Chain Lightning',
  'Healing Word',
  'Shadow Step'
]

spellbook.append('Time Stop')
spellbook.remove('Healing Word')
spellbook.pop(1)

print(spellbook)
```


## 05. Iteración sobre una Lista (`soundtrack.py`)

### 🔹 Iteración Directa (`for-in`)

Itera directamente sobre los elementos de la lista.


```python
boss_health = [320, 280, 410, 190, 540, 260, 130]

for i in boss_health:
  print(i)
```


### 🔹 Iteración Basada en Índices (`for-in` con `range()` y `len()`)

Itera a través de los índices usando `range(len(list))`.


```python
boss_health = [320, 280, 410, 190, 540, 260, 130]

for i in range(len(boss_health)):
  print(boss_health[i])
```


### 📝 Ejercicio de Banda Sonora (`soundtrack.py`)


```python
# soundtrack.py

playlist = [
  'Boss Rush Overture',
  'Overture of the Kingdom',
  'Tavern at Dusk',
  'Echoing Caverns',
  'Final Boss Concerto',
  'Victory Fanfare'
]

for song in playlist:
  print(song)
```
