

## 06. Bucket List Project (`bucket_list.py`)

Combining concepts of list creation and iteration to output a bucket list.


### 📝 Bucket List Exercise (`bucket_list.py`)

```python
# bucket_list.py

things_to_do = [
  'Create the dopest learn to code platform ever.',
  'Hike the Pacific Crest Trail.',
  'Build an A-frame house and raise some goats.',
  'Live somewhere in Asia for a year.',
  'Release an album.',
  'Write a book.',
  'Reach 100k subscribers on YouTube.',
  'Road trip with the fam.',
  'Open a cozy diner upstate.',
  'Grow old with no regrets.'
]

for thing in things_to_do:
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


#### Tic-Tac-Toe Board Example


```python
board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]

# Accessing row 2, column 1
row = 2
column = 1
print(board[row][column]) # Output: x
```


---
type: note
course: Codedex Python
chapter: Lists
topic: Dictionaries and Sets
tags:
  - python
  - data-structures
  - dictionaries
  - sets
---


# Bonus: Dictionaries & Sets in Python

Python offers structures beyond standard ordered lists that enable faster searches, optimized organization, and direct value retrieval.

---


## 1. Dictionaries

A **dictionary** connects a unique `key` to a `value`. They are ordered collections storing data as `key: value` pairs.

```python
contacts = {
    'Taylor': '626-242-1072',
    'Xin Xin': '614-555-5678',
    'Hans': '614-555-9999'
}
```


### Accessing Values

Items are retrieved using key indexing `[key]` instead of zero-based numerical indices:


```python
print(contacts['Xin Xin']) 
# Output: 614-555-5678
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
|`.keys()`|Returns all dictionary keys|`dict_keys(['Taylor', 'Xin Xin', 'Hans'])`|
|`.values()`|Returns all values|`dict_values(['626-242-1072', ...])`|
|`.items()`|Returns a list of `(key, value)` tuples|`dict_items([('Taylor', '626-242-1072'), ...])`|


```python
print(contacts.keys())
print(contacts.values())
print(contacts.items())
```


## 2. Sets

A **set** is an unordered collection of **unique items** with no duplicates.


```python
mochi_favorites = {'Tuna', 'Chestnuts', 'Corn', 'Valerian Root Tea', 'Catnip'}
cloud_favorites = {'Salmon', 'Chicken', 'Catnip', 'Sweet Potato', 'Rice'}
```

> [!WARNING] Creating Empty Sets Declaring `{}` creates an empty **dictionary**, not a set. To initialize an empty set, use `set()`:
> 
> 
```python
empty_set = set()
```
> 
> 


### Set Methods

- **`.union()`**: Combines items from both sets.
    
- **`.intersection()`**: Finds elements present in both sets.
    
- **`.difference()`**: Finds elements unique to the calling set.
    

Python

```
# Union
print(mochi_favorites.union(cloud_favorites))

# Intersection
print(mochi_favorites.intersection(cloud_favorites))
# Output: {'Catnip'}

# Difference
print(mochi_favorites.difference(cloud_favorites))
# Output: {'Tuna', 'Chestnuts', 'Corn', 'Valerian Root Tea'}
```

## Summary: Data Structures Overview

|Data Structure|Characteristics|Common Use Case|
|---|---|---|
|**List**|Ordered, index-accessible, allows duplicates|Grocery lists, chronological logs|
|**Dictionary**|Key-value pairs, fast key lookups|Contact lists, configuration profiles|
|**Set**|Unordered, unique elements, fast membership checks|Filtering duplicates, comparing categories|


