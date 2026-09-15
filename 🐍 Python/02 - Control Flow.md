---
course: Python
tags:
  - python
  - control-flow
  - logic
  - fundamentals
type: lesson
---

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

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


---

## 04. Relational Operators & `elif` Statements

Relational operators compare two values and return a boolean result (`True` or `False`):

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to


### 🔹 The `elif` Statement
When checking more than two conditions, append `elif` (else if) blocks between `if` and `else`.

```python
rating = 4.8

if rating >= 4.5:
  print('Masterpiece 🌟')
elif rating >= 3.5:
  print('Recommended 👍')
elif rating >= 2.5:
  print('Average 😐')
else:
  print('Needs Improvement 👎')
```


### 🧪 Chemical Solution Analysis (`ph_levels.py`)

Checks liquid pH levels to determine chemical properties:

```python
# ph_levels.py

ph = float(input('Enter pH level (0-14): '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
```


## 05. Generating Random Values (`magic8.py`)

Python's built-in `random` module provides functions like `randint(a, b)` to produce random integers within a range $[a, b]$ inclusive.

```python
import random

# Generate an option between 1 and 9
option = random.randint(1, 9)

prompt = input('Ask a decision question: ')

if option == 1:
  answer = 'Yes - definitely.'
elif option == 2:
  answer = 'It is decidedly so.'
elif option == 3:
  answer = 'Without a doubt.'
elif option == 4:
  answer = 'Reply hazy, try again.'
elif option == 5:
  answer = 'Ask again later.'
elif option == 6:
  answer = 'Better not tell you now.'
elif option == 7:
  answer = 'My sources say no.'
elif option == 8:
  answer = 'Outlook not so good.'
else:
  answer = 'Very doubtful.'

print('Question: ' + prompt)
print('Magic 8 Ball: ' + answer)
```



## 06. Logical Operators

Logical operators evaluate and combine multiple boolean expressions:

- `and`: Returns `True` only if **both** conditions evaluate to `True`.
    
- `or`: Returns `True` if **at least one** condition evaluates to `True`.
    
- `not`: Reverses the boolean status (`True` becomes `False`).
    

|**A**|**B**|**A and B**|**A or B**|
|---|---|---|---|
|`False`|`False`|`False`|`False`|
|`False`|`True`|`False`|`True`|
|`True`|`False`|`False`|`True`|
|`True`|`True`|`True`|`True`|


```python
# Practical Examples
energy = 8
focus = 6

if energy > 5 and focus > 5:
  print('Optimal coding session!')

has_coffee = True
has_tea = False

if has_coffee or has_tea:
  print('Caffeine acquired ☕')

is_busy = False

if not is_busy:
  print('Ready to commit code!')
```




### 🎢 Theme Park Access Checker (`the_cyclone.py`)

Evaluates height requirement ($140\text{ cm}$) and entry credits ($15\text{ credits}$):

```python
# the_cyclone.py

height = int(input('Enter your height in cm: '))
credits = int(input('Enter your available credits: '))

if height >= 140 and credits >= 15:
  print('Enjoy the ride!')
elif credits >= 15 and height < 140:
  print('You are not tall enough to ride.')
elif height >= 140 and credits < 15:
  print("You don't have enough credits.")
else:
  print('Requirements not met for entry.')
```


## 7. Capstone Project: Guild Sorting Quiz (`sorting_hat.py`)

```python
# sorting_hat.py

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Q1) Do you prefer Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')
q1_answer = int(input('Answer (1-2): '))

if q1_answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1_answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Invalid input.')

print('\nQ2) When I am done with a project, I want to be remembered as:')
print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')
q2_answer = int(input('Answer (1-4): '))

if q2_answer == 1:
  hufflepuff += 2
elif q2_answer == 2:
  slytherin += 2
elif q2_answer == 3:
  ravenclaw += 2
elif q2_answer == 4:
  gryffindor += 2
else:
  print('Invalid input.')

print('\nQ3) Which style of sound inspires your creative focus?')
print('  1) Classical Violin')
print('  2) Energetic Brass')
print('  3) Ambient Piano')
print('  4) Rhythm Drums')
q3_answer = int(input('Answer (1-4): '))

if q3_answer == 1:
  slytherin += 4
elif q3_answer == 2:
  hufflepuff += 4
elif q3_answer == 3:
  ravenclaw += 4
elif q3_answer == 4:
  gryffindor += 4
else:
  print('Invalid input.')

print('\n--- Final Scores ---')
print('Gryffindor:', gryffindor)
print('Ravenclaw:', ravenclaw)
print('Hufflepuff:', hufflepuff)
print('Slytherin:', slytherin)
```





