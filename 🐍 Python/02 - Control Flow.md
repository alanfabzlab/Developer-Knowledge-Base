
---
tags:
  - python
  - control-flow
  - logic
  - fundamentals
status: in-progress
type: lesson
---

# 🔀 Python Control Flow & Error Handling

![Status Badge](https://img.shields.io/badge/Topic-Control%20Flow-orange?style=for-the-badge)

---

## 01. Common Errors in Python

Errors are a natural part of programming. Recognizing error types helps debug code faster.

### 📌 Main Error Types

- **`SyntaxError`**: Occurs when code violates Python's syntax rules (misspelled keywords, missing quotes, or invalid structure).
- **`NameError`**: Occurs when referencing a variable or function that hasn't been defined yet.
- **`TypeError`**: Occurs when applying an operation to an incompatible data type (e.g., combining strings and integers without casting).

---

### 🔍 Error Examples & Solutions

#### ❌ SyntaxError Example

```python
# Error: Missing closing quote and proper syntax
print(Welcome to Python!

# SyntaxError: invalid syntax
```

#### ❌ NameError Example

```python
# Error: Referencing an undefined variable
print(player_score)

# NameError: name 'player_score' is not defined

# Fix: Define the variable before referencing it
player_score = 100
print(player_score)  # Output: 100
```

#### ❌ TypeError Example

```python
# Error: Attempting string concatenation with an integer directly
status = 'Current Level: '
print(status + 5)

# TypeError: can only concatenate str (not "int") to str

# Fix: Cast integer using str()
status = 'Current Level: '
print(status + str(5))  # Output: Current Level: 5
```

🐛 Bug Catcher Debugging Challenge (`bug_catcher.py`)

```python
# Fixed version of inventory tracking script
health_potions = 5
mana_potions = 8
stamina_potions = 12

print('Inventory: ' + str(health_potions) + ' Health Potions')
print('Inventory: ' + str(mana_potions) + ' Mana Potions')
print('Inventory: ' + str(stamina_potions) + ' Stamina Potions')

total_potions = health_potions + mana_potions + stamina_potions
print('Total items: ' + str(total_potions) + ' potions collected!')
```

## 02. Control Flow & Decision Making

By default, Python runs code sequentially line by line. **Control Flow** allows programs to execute different code blocks depending on specific conditions.

> [!NOTE] Concept Think of control flow as a crossroads: if a condition evaluates to `True`, the program takes one path; if `False`, it takes another.


### 🪙 Coin Flip Simulation (`coin_flip.py`)

Using the `random` module to execute conditional code blocks based on a generated number:

```python
# coin_flip.py
import random

# Generate a random integer: 0 or 1
num = random.randint(0, 1)

if num > 0.5:
  print('Heads 🪙')
else:
  print('Tails 🪙')
```


## 03. Conditional Statements: `if` & `else`

### 🔹 `if` Statement

Evaluates a condition. If the condition is `True`, the indented block underneath runs.

```python
score = 75

if score >= 60:
  print('Requirement Met! ✅')
```


### 🔹 `else` Clause

Provides an alternative execution block when the `if` condition evaluates to `False`.

```python
score = 45

if score >= 60:
  print('Requirement Met! ✅')
else:
  print('Requirement Not Met! ❌')
```


### 📊 Academic Grade Checker (`grades.py`)

Checks whether a student's grade meets the minimum passing threshold (55):

```python
# grades.py

# Assigned test score (Range 0-100)
grade = 78

if grade >= 55:
  print('You passed!')
else:
  print('You failed.')
```


