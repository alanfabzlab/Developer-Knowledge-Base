<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 05 - Lists

A **list** is an ordered collection of items stored in a single variable. Lists are defined using square brackets `[]` with items separated by commas.

---

## 01. Introduction to Lists (`grocery.py`)

Lists can hold multiple data items, duplicate values, and mixed data types without a size limit.

```python
# Storing data using lists
hw_grades = [98, 87, 92, 96]
quiz_grades = [9, 6, 8]
````


### 📝 Grocery List Exercise (`grocery.py`)


```python
# grocery.py

grocery = ['Eggs', 'Avocados', 'Cookies', 'Hot Pepper Jam', 'Blueberries', 'Broccoli']
print(grocery)
```


## 02. Indexing, Slicing & Errors (`todo.py`)

### 🔹 Indexing

List items are accessed via their zero-based position index `[index]`. Negative indices count backward from the end (`-1` is the last item).


```python
vowels = ['a', 'e', 'i', 'o', 'u']
# Positive Index: 0, 1, 2, 3, 4
# Negative Index: -5, -4, -3, -2, -1

print(vowels[0])   # Output: a
print(vowels[-1])  # Output: u
```


### 🔹 Slicing

Slicing retrieves a sub-sequence of items using `[start:end]`. It includes the `start` index and excludes the `end` index.


```python
vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels[0:3]) # Output: ['a', 'e', 'i']
print(vowels[1:3]) # Output: ['e', 'i']
```


### 🔹 IndexError

An `IndexError` occurs when attempting to access an index that exceeds the sequence bounds.


```python
# Causes Traceback: IndexError: list index out of range
print(vowels[5]) 
```


### 📝 To-Do List Exercise (`todo.py`)


```python
# todo.py

todo = [
  'Get quarters.',
  'Do laundry.',
  'Take a walk.',
  'Get a haircut.',
  'Make some tea.',
  'Complete Lists chapter.',
  'Call mom.',
  'Watch My Hero Academia.'
]

# Print first and second items
print(todo[0])
print(todo[1])

# Slice third, fourth, and fifth items
print(todo[2:5])

# Accessing index 9 causes IndexError
# print(todo[9])
```



## 03. Built-in Functions (`inventory.py`)

Python includes several built-in functions designed to work directly with lists:

* `len()`: Returns the total number of items in a list.
* `max()`: Returns the maximum value in a list.
* `min()`: Returns the minimum value in a list.


```python
stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

print(len(stock1_prices)) # Output: 7
print(max(stock1_prices)) # Output: 2.52
print(min(stock2_prices)) # Output: 8.11
```



### 📝 Inventory Exercise (`inventory.py`)


```python
# inventory.py

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1203]

# Lowest quantity LEGO part
print(min(lego_parts))

# Highest quantity LEGO part
print(max(lego_parts))
```


## 04. List Methods (`reading_list.py`)

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
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')       # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')    # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')       # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)              # ['GAU', 'UCG', 'UAA']
```


### 📝 Reading List Exercise (`reading_list.py`)


```python
# reading_list.py

books = [
  'Harry Potter',
  '1984',
  'The Fault in Our Stars',
  'The Mom Test',
  'Life in Code'
]

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)
```


## 05. Iterating Over a List (`mixtape.py`)

### 🔹 Direct Iteration (`for-in`)

Iterates directly over the items of the list.


```python
snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in snowfall:
  print(i)
```


### 🔹 Index-Based Iteration (`for-in` with `range()` and `len()`)

Iterates through indices using `range(len(list))`.


```python
snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in range(len(snowfall)):
  print(snowfall[i])
```


### 📝 Mixtape Exercise (`mixtape.py`)


```python
# mixtape.py

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Hank Heaven - Threads',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

for song in playlist:
  print(song)
```


