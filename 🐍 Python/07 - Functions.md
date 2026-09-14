---
tags:
  - python
  - programming
  - functions
  - dry
  - open-source
  - notes
status: in-progress
type: lesson
---

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🐍 Python Functions & Modern Syntax

![Status Badge](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge&logo=python&logoColor=white)

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />


## 01. The D.R.Y. Principle & Built-in Functions (`dry.py`)

A **function** is a reusable block of code that performs a specific task. Instead of repeating code blocks throughout a program, you can wrap code inside a function and execute it whenever needed.


### 🔹 The D.R.Y. Principle
**D.R.Y.** stands for **"Don't Repeat Yourself"**, a fundamental software development principle aimed at reducing code repetition and writing clean, maintainable logic.


### 🔹 Built-in Functions
Python includes 68 built-in functions ready to use out of the box (e.g., `print()`, `input()`, `len()`, `int()`, `type()`).


### 📝 D.R.Y. Exercise (`dry.py`)


```python
# dry.py

# print() prints text or values to the console
print('Hola, Codédex!')

# input() requests user input from the console
nombre = input('¿Cuál es tu nombre? ')

# len() returns the length or number of elements
longitud = len(nombre)

# int() converts a value into an integer
edad = int('25')

# type() returns the data type of an object
print(type(nombre))
```



## 02. Defining & Calling Functions (`fortune_cookie.py`)

User-defined functions require two key steps:

1. **Definition**: Created using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. Code inside must be indented.
    
2. **Execution (Call)**: Triggered by writing the function name followed by parentheses `()`.
    



### 📝 Fortune Cookie Exercise (`fortune_cookie.py`)


```python
# fortune_cookie.py
import random

def fortune():
  random_fortune = random.randint(1, 8)

  if random_fortune == 1:
    print('Don\'t pursue happiness - create it.')
  elif random_fortune == 2:
    print('All things are difficult before they are easy.')
  elif random_fortune == 3:
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif random_fortune == 4:
    print('Someone in your life needs a letter from you.')
  elif random_fortune == 5:
    print('Don\'t just think. Act!')
  elif random_fortune == 6:
    print('Your heart will skip a beat.')
  elif random_fortune == 7:
    print('The fortune you search for is in another cookie.')
  else:
    print('Help! I\'m being held prisoner in a Chinese bakery!')

# Function calls
fortune()
fortune()
fortune()
```


## 03. Parameters and Arguments

Functions become dynamic when they accept input data to process.

- **Parameter**: The variable defined inside the function's parentheses (the placeholder).
    
- **Argument**: The actual value passed into the function when calling it.
    


```python
# 'name' is the parameter
def happy_birthday(name):
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear ' + name)
  print('Happy birthday to you')

# 'Lillian' is the argument
happy_birthday('Lillian')
```

