# 06 - Funciones Integradas y Métodos de Lista

**Versión original en inglés:** [06 - Built-in Functions & List Methods.md](./06%20-%20Built-in%20Functions%20&%20List%20Methods.md)

**Curso:** Python
**Tema:** Funciones integradas, métodos de lista, listas anidadas y matrices, diccionarios, conjuntos
**Etiquetas:** `#python` `#list-methods` `#built-in-functions` `#data-structures` `#iteration`

## 06. Proyecto de Registro de Boss Rush (`boss_rush_log.py`)

Combina los conceptos de creación e iteración de listas para producir un registro de boss rush.


### 📝 Ejercicio de Registro de Boss Rush (`boss_rush_log.py`)

```python
# boss_rush_log.py

things_to_beat = [
  'Slay the Chrono Warden with a pistol only.',
  'Clear the Sunken Keep without healing items.',
  'Beat the entire raid with four players.',
  'Finish the campaign on Nightmare difficulty.',
  'Speedrun the Ashwood Mines under 10 minutes.',
  'Collect every golden key in the kingdom.',
  'Survive 100 waves of the endless mode.',
  'Build a working game and ship it.',
  'Playtest with strangers and take notes.',
  'Never rage quit. Never again.'
]

for thing in things_to_beat:
  print(thing)
```



## 07. Listas Anidadas y Matrices

Una **lista anidada** es una lista que contiene otras listas como elementos.

```python
# Mixed nested list
my_list = ['a', 'b', 'c', [1, 2, 3]]

# Accessing elements inside a nested list
print(my_list[3][1]) # Output: 2
```



### 🔹 Matrices (Listas 2D)

Cuando todos los elementos de una lista son listas anidadas de la misma longitud, se forma una **matriz** o **lista 2D** (organizada en filas y columnas).


```python
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
```


#### Ejemplo de Mapa de Batalla


```python
battle_map = [
  ['M', 'M', 'M'],
  ['M', 'B', 'M'],
  ['S', 'B', 'T']
]

# Legend: M = mountain, B = boss spawn, S = shop, T = treasure

# Accessing row 2, column 1
row = 2
column = 1
print(battle_map[row][column]) # Output: B
```


---


## Bonus: Diccionarios y Conjuntos en Python

Python ofrece estructuras más allá de las listas ordenadas estándar que permiten búsquedas más rápidas, organización optimizada y recuperación directa de valores.

---


## 1. Diccionarios

Un **diccionario** conecta una `key` única con un `value`. Son colecciones ordenadas que almacenan datos como pares `key: value`.

```python
party = {
    'Aria': 'Ranger',
    'Kai': 'Paladin',
    'Nyx': 'Mage'
}
```


### Accediendo a los Valores

Los elementos se recuperan usando indexación por clave `[key]` en lugar de índices numéricos basados en cero:


```python
print(party['Nyx']) 
# Output: Mage
```

**Nota:** Reglas de las Claves

- Cada **key** debe ser única.

- Las **keys** se asignan directamente a valores (cualquier tipo de dato).

- Las **keys** son inmutables y no se pueden modificar después de crearse.


### Métodos del Diccionario

|Método|Descripción|Salida de Ejemplo|
|---|---|---|
|`.keys()`|Devuelve todas las claves del diccionario|`dict_keys(['Aria', 'Kai', 'Nyx'])`|
|`.values()`|Devuelve todos los valores|`dict_values(['Ranger', 'Paladin', 'Mage'], ...)`|
|`.items()`|Devuelve una lista de tuplas `(key, value)`|`dict_items([('Aria', 'Ranger'), ...])`|


```python
print(party.keys())
print(party.values())
print(party.items())
```


## 2. Conjuntos

Un **conjunto** es una colección no ordenada de **elementos únicos** sin duplicados.


```python
loot_favorites = {'Sword', 'Shield', 'Potion', 'Helm', 'Boots'}
spell_favorites = {'Staff', 'Wand', 'Potion', 'Scroll', 'Rune'}
```

**Advertencia:** Crear Conjuntos Vacíos Declarar `{}` crea un **diccionario** vacío, no un conjunto. Para inicializar un conjunto vacío, usa `set()`:


```python
empty_set = set()
```


### Métodos del Conjunto

- **`.union()`**: Combina los elementos de ambos conjuntos.
    
- **`.intersection()`**: Encuentra los elementos presentes en ambos conjuntos.
    
- **`.difference()`**: Encuentra los elementos únicos del conjunto que llama.
    

Python

```python
# Union
print(loot_favorites.union(spell_favorites))

# Intersection
print(loot_favorites.intersection(spell_favorites))
# Output: {'Potion'}

# Difference
print(loot_favorites.difference(spell_favorites))
# Output: {'Sword', 'Shield', 'Helm', 'Boots'}
```

## Resumen: Visión General de Estructuras de Datos

|Estructura de Datos|Características|Caso de Uso Común|
|---|---|---|
|**Lista**|Ordenada, accesible por índice, permite duplicados|Bolsas de botín, registros de combate|
|**Diccionario**|Pares clave-valor, búsquedas de claves rápidas|Archivos de guardado, configuraciones de habilidades|
|**Conjunto**|Elementos no ordenados y únicos, comprobaciones de pertenencia rápidas|Filtrar buffs duplicados, comparar configuraciones|
