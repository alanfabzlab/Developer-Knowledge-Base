

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