
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🐍 Python Functions & Modern Syntax

![Status Badge](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge&logo=python&logoColor=white)

**Course:** Python
**Topic:** Function Definition, Parameters, Return Values, Variable Scope & Lambda Functions
**Tags:** `#python` `#programming` `#functions` `#dry` `#open-source` `#notes`


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
print('Ready Player One!')

# input() requests user input from the console
hero = input('Enter your hero name: ')

# len() returns the length or number of elements
name_length = len(hero)

# int() converts a value into an integer
level = int('25')

# type() returns the data type of an object
print(type(hero))
```



## 02. Defining & Calling Functions (`loot_box.py`)

User-defined functions require two key steps:

1. **Definition**: Created using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`. Code inside must be indented.
    
2. **Execution (Call)**: Triggered by writing the function name followed by parentheses `()`.
    



### 📝 Loot Box Oracle Exercise (`loot_box.py`)


```python
# loot_box.py
import random

def loot_box():
  random_fortune = random.randint(1, 8)

  if random_fortune == 1:
    print('Don\'t grind for the meta build - invent one.')
  elif random_fortune == 2:
    print('All bosses are hard before they are farmed.')
  elif random_fortune == 3:
    print('The early bird gets the loot, but the second raid gets the legend.')
  elif random_fortune == 4:
    print('Someone in your party needs a health potion from you.')
  elif random_fortune == 5:
    print('Don\'t just think. Press attack!')
  elif random_fortune == 6:
    print('Your heart will skip a beat at 1 HP.')
  elif random_fortune == 7:
    print('The drop you are grinding for is in another chest.')
  else:
    print('Help! I\'m trapped in a cutscene!')


# Function calls
loot_box()
loot_box()
loot_box()
```


## 03. Parameters and Arguments

Functions become dynamic when they accept input data to process.

- **Parameter**: The variable defined inside the function's parentheses (the placeholder).
    
- **Argument**: The actual value passed into the function when calling it.
    


```python
# 'hero' is the parameter
def level_up(hero):
  print('Level up for the hero')
  print('Level up for the hero')
  print('Level up, dear ' + hero)
  print('Level up for the hero')

# 'Aria' is the argument
level_up('Aria')
```



## 04. Return Value


A function can return a value back to the line of code that called it using the `return` keyword. 


* **`return`**: Ends the execution of a function and sends data back to the caller.
* **Implicit Return**: If no `return` statement is defined, Python returns `None` by default.
* **`print()` vs `return`**: `print()` only displays output to the terminal, whereas `return` passes data internally so it can be saved in variables or processed further.


```python
# Exercise 31: Damage Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    return a ** b

# Output execution
print(add(18, 7))        # Output: 25
print(subtract(18, 7))   # Output: 11
print(multiply(18, 7))   # Output: 126
print(divide(18, 6))     # Output: 3.0
print(exp(2, 10))        # Output: 1024
```



## 05. Variable Scope

Scope determines where in the program a variable is visible and accessible.

- **Local Scope**: Variables declared inside a function. They only exist while the function is executing and cannot be accessed from outside.
    
- **Global Scope**: Variables declared outside of any function. They are accessible throughout the entire script.
    


```python
# Exercise 32: Damage Log (Time Series Analysis)
damage_per_turn = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.91, 43.87]

def damage_at(x):
    # 'x' is a local variable, 'damage_per_turn' is global
    return damage_per_turn[x - 1]

def max_damage(a, b):
    return max(damage_per_turn[a - 1:b])

def min_damage(a, b):
    return min(damage_per_turn[a - 1:b])

# Tests
print(f"Damage on turn 3: {damage_at(3)}")
print(f"Max damage (turns 1-5): {max_damage(1, 5)}")
print(f"Min damage (turns 5-10): {min_damage(5, 10)}")
```



## 06. Checkpoint Project: Blacksmith

Integrating functions, user input, conditional structures, and returned values into a single program.


```python
# Exercise 33: Blacksmith
def welcome():
    print("Welcome to the Blacksmith!")
    print("1. ⚔️ Iron Sword")
    print("2. 🛡️ Leather Shield")
    print("3. 🧪 Health Potion")
    print("4. 🌀 Teleport Scroll")
    print("5. 🔑 Golden Key")

def get_item(x):
    if x == 1:
        return 'Iron Sword'
    elif x == 2:
        return 'Leather Shield'
    elif x == 3:
        return 'Health Potion'
    elif x == 4:
        return 'Teleport Scroll'
    elif x == 5:
        return 'Golden Key'
    else:
        return 'Invalid item'

# Execution flow
welcome()
option = int(input('What would you like to buy? '))
print(f"You bought: {get_item(option)}")
```


---

## 07. Lambda Functions (Bonus Article)

Lambda functions (also known as anonymous functions) are concise, single-line functions defined without a name using the `lambda` keyword.

### Syntax

```python
lambda arguments: expression
```


- **`lambda`**: Keyword used to define an anonymous function.
    
- **`arguments`**: Inputs passed to the function (separated by commas).
    
- **`expression`**: A single expression evaluated and returned automatically.
    



### Basic Example vs. Standard Function

**Standard Function:**


```python
def double_damage(x):
    return x * 2
```


**Lambda Equivalent:**


```python
double_damage = lambda x: x * 2

print(double_damage(4)) # Output: 8
```


### Common Use Cases: `map()` & `filter()`

Lambda functions shine when passed as one-time arguments to high-order functions like `map()` or `filter()`.


```python
damage_values = [2, 4, 6, 8, 10]

# Using map() to double each element
doubled_damage = list(map(lambda x: x * 2, damage_values))

# Using filter() to keep only the heavy hits
heavy_hits = list(filter(lambda x: x > 7, damage_values))

print(doubled_damage) # Output: [4, 8, 12, 16, 20]
print(heavy_hits)     # Output: [8, 10]
```


### Practical Examples

**1. Filtering Text Data:**


```python
heroes = ['Aria', 'Borin', 'Cass', 'Dara', 'Elowen']

# Filter out hero names starting with 'A'
filtered_heroes = list(filter(lambda name: name[0].upper() != 'A', heroes))

print(filtered_heroes) # Output: ['Borin', 'Cass', 'Dara', 'Elowen']
```


**2. Using Multiple Arguments:**


```python
spell_name = lambda str1, str2: str1 + str2

name = spell_name('fire', 'ball')
print(f'The spell name is: {name}') # Output: The spell name is: fireball
```
