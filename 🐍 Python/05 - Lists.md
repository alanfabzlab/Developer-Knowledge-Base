

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 05 - Lists

> [!INFO] Metadata
> **Course:** Python
> **Topic:** Python Lists, Indexing & Slicing, Built-in Functions, List Methods, Iterating Over Lists
> **Tags:** `#python` `#lists` `#data-structures` `#arrays` `#fundamentals`


A **list** is an ordered collection of items stored in a single variable. Lists are defined using square brackets `[]` with items separated by commas.

---

## 01. Introduction to Lists (`boss_stats.py`)

Lists can hold multiple data items, duplicate values, and mixed data types without a size limit.

```python
# Storing data using lists
boss_hp = [980, 870, 920, 960]
wave_damage = [9, 6, 8]
```


### 📝 Loot Bag Exercise (`loot_bag.py`)


```python
# loot_bag.py

loot_bag = ['Health Potion', 'Iron Sword', 'Bomb Rune', 'Teleport Scroll', 'Golden Key', 'Monster Pelt']
print(loot_bag)
```


## 02. Indexing, Slicing & Errors (`quest_log.py`)

### 🔹 Indexing

List items are accessed via their zero-based position index `[index]`. Negative indices count backward from the end (`-1` is the last item).


```python
elements = ['Fire', 'Ice', 'Lightning', 'Earth', 'Wind']
# Positive Index: 0, 1, 2, 3, 4
# Negative Index: -5, -4, -3, -2, -1

print(elements[0])   # Output: Fire
print(elements[-1])  # Output: Wind
```


### 🔹 Slicing

Slicing retrieves a sub-sequence of items using `[start:end]`. It includes the `start` index and excludes the `end` index.


```python
elements = ['Fire', 'Ice', 'Lightning', 'Earth', 'Wind']

print(elements[0:3]) # Output: ['Fire', 'Ice', 'Lightning']
print(elements[1:3]) # Output: ['Ice', 'Lightning']
```


### 🔹 IndexError

An `IndexError` occurs when attempting to access an index that exceeds the sequence bounds.


```python
# Causes Traceback: IndexError: list index out of range
print(elements[5]) 
```


### 📝 Quest Log Exercise (`quest_log.py`)


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



## 03. Built-in Functions (`inventory.py`)

Python includes several built-in functions designed to work directly with lists:

* `len()`: Returns the total number of items in a list.
* `max()`: Returns the maximum value in a list.
* `min()`: Returns the minimum value in a list.


```python
potion_prices = [12.50, 9.75, 15.20, 9.75, 18.40, 11.30, 13.60]
rune_prices = [45.10, 32.80, 51.25, 28.40, 39.95, 28.40, 33.60]

print(len(potion_prices)) # Output: 7
print(max(potion_prices)) # Output: 18.4
print(min(rune_prices)) # Output: 28.4
```



### 📝 Loot Tracker Exercise (`loot_tracker.py`)


```python
# loot_tracker.py

enemy_kills = [452, 318, 197, 806, 645, 274, 903, 261]

# Lowest kill count enemy
print(min(enemy_kills))

# Highest kill count enemy
print(max(enemy_kills))
```


## 04. List Methods (`spellbook.py`)

List methods are called using dot notation (`list_name.method()`).

|**Method**|**Description**|
|---|---|
|`.append()`|Adds an item to the end of the list|
|`.clear()`|Removes all items from the list|
|`.copy()`|Returns a shallow copy of the list|
|`.count()`|Returns the number of times a value appears|
|`.extend()`|Appends another list to the current list|
|`.index()`|Returns the index of a value inside the list|
|`.insert()`|Inserts an item at a specified position|
|`.pop()`|Removes an item from a specified position|
|`.remove()`|Removes the first item with the specified value|
|`.reverse()`|Reverses the order of the list in place|
|`.sort()`|Sorts the list in place|



### 🔹 Example Usage


```python
loot_codes = ['SWD', 'SHT', 'BOW', 'POT']

loot_codes.append('RIN')      # ['SWD', 'SHT', 'BOW', 'POT', 'RIN']
loot_codes.insert(2, 'HEL')   # ['SWD', 'SHT', 'HEL', 'BOW', 'POT', 'RIN']
loot_codes.remove('SHT')      # ['SWD', 'HEL', 'BOW', 'POT', 'RIN']
loot_codes.pop(0)             # ['HEL', 'BOW', 'POT', 'RIN']
```


### 📝 Spellbook Exercise (`spellbook.py`)


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


## 05. Iterating Over a List (`soundtrack.py`)

### 🔹 Direct Iteration (`for-in`)

Iterates directly over the items of the list.


```python
boss_health = [320, 280, 410, 190, 540, 260, 130]

for i in boss_health:
  print(i)
```


### 🔹 Index-Based Iteration (`for-in` with `range()` and `len()`)

Iterates through indices using `range(len(list))`.


```python
boss_health = [320, 280, 410, 190, 540, 260, 130]

for i in range(len(boss_health)):
  print(boss_health[i])
```


### 📝 Soundtrack Exercise (`soundtrack.py`)


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
