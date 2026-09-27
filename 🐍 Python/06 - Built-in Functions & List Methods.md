# 06 - Built-in Functions & List Methods

> [!INFO] Metadata
> **Course:** Python
> **Topic:** Built-in Functions, List Methods, Nested Lists & Matrices, Dictionaries, Sets
> **Tags:** `#python` `#list-methods` `#built-in-functions` `#data-structures` `#iteration`

## 06. Boss Rush Log Project (`boss_rush_log.py`)

Combining concepts of list creation and iteration to output a boss rush log.


### 📝 Boss Rush Log Exercise (`boss_rush_log.py`)

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



## 07. Nested Lists & Matrices

A **nested list** is a list that contains other lists as elements.

```python
# Mixed nested list
my_list = ['a', 'b', 'c', [1, 2, 3]]

# Accessing elements inside a nested list
print(my_list[3][1]) # Output: 2
```



### 🔹 Matrices (2D Lists)

When every item in a list is a nested list of equal length, it forms a **matrix** or **2D list** (organized in rows and columns).


```python
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
```


#### Battle Map Example


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


## Bonus: Dictionaries & Sets in Python

Python offers structures beyond standard ordered lists that enable faster searches, optimized organization, and direct value retrieval.

---


## 1. Dictionaries

A **dictionary** connects a unique `key` to a `value`. They are ordered collections storing data as `key: value` pairs.

```python
party = {
    'Aria': 'Ranger',
    'Kai': 'Paladin',
    'Nyx': 'Mage'
}
```


### Accessing Values

Items are retrieved using key indexing `[key]` instead of zero-based numerical indices:


```python
print(party['Nyx']) 
# Output: Mage
```

> [!NOTE] Key Rules
> 
> - Each **key** must be unique.
>     
> - **Keys** map directly to values (any data type).
>     
> - **Keys** are immutable and cannot be modified after creation.
>     


### Dictionary Methods

|Method|Description|Example Output|
|---|---|---|
|`.keys()`|Returns all dictionary keys|`dict_keys(['Aria', 'Kai', 'Nyx'])`|
|`.values()`|Returns all values|`dict_values(['Ranger', 'Paladin', 'Mage'], ...)`|
|`.items()`|Returns a list of `(key, value)` tuples|`dict_items([('Aria', 'Ranger'), ...])`|


```python
print(party.keys())
print(party.values())
print(party.items())
```


## 2. Sets

A **set** is an unordered collection of **unique items** with no duplicates.


```python
loot_favorites = {'Sword', 'Shield', 'Potion', 'Helm', 'Boots'}
spell_favorites = {'Staff', 'Wand', 'Potion', 'Scroll', 'Rune'}
```

> [!WARNING] Creating Empty Sets Declaring `{}` creates an empty **dictionary**, not a set. To initialize an empty set, use `set()`:
> 
> 
> ```python
> empty_set = set()
> ```
> 
> 


### Set Methods

- **`.union()`**: Combines items from both sets.
    
- **`.intersection()`**: Finds elements present in both sets.
    
- **`.difference()`**: Finds elements unique to the calling set.
    

Python

```
# Union
print(loot_favorites.union(spell_favorites))

# Intersection
print(loot_favorites.intersection(spell_favorites))
# Output: {'Potion'}

# Difference
print(loot_favorites.difference(spell_favorites))
# Output: {'Sword', 'Shield', 'Helm', 'Boots'}
```

## Summary: Data Structures Overview

|Data Structure|Characteristics|Common Use Case|
|---|---|---|
|**List**|Ordered, index-accessible, allows duplicates|Loot bags, combat logs|
|**Dictionary**|Key-value pairs, fast key lookups|Save files, ability loadouts|
|**Set**|Unordered, unique elements, fast membership checks|Filtering duplicate buffs, comparing loadouts|
