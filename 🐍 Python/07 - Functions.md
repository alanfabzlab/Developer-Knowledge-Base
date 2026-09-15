---
course: Python
tags:
  - python
  - programming
  - functions
  - dry
  - open-source
  - notes
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



## 04. Return Value


A function can return a value back to the line of code that called it using the `return` keyword. 


* **`return`**: Ends the execution of a function and sends data back to the caller.
* **Implicit Return**: If no `return` statement is defined, Python returns `None` by default.
* **`print()` vs `return`**: `print()` only displays output to the terminal, whereas `return` passes data internally so it can be saved in variables or processed further.


```python
# Exercise 31: Calculator
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
print(add(10, 5))       # Output: 15
print(subtract(10, 5))  # Output: 5
print(multiply(10, 5))  # Output: 50
print(divide(10, 5))    # Output: 2.0
print(exp(2, 3))        # Output: 8
```



## 05. Variable Scope

Scope determines where in the program a variable is visible and accessible.

- **Local Scope**: Variables declared inside a function. They only exist while the function is executing and cannot be accessed from outside.
    
- **Global Scope**: Variables declared outside of any function. They are accessible throughout the entire script.
    


```python
# Exercise 32: Stonks (Time Series Analysis)
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.91, 43.87]

def price_at(x):
    # 'x' is a local variable, 'stock_prices' is global
    return stock_prices[x - 1]

def max_price(a, b):
    return max(stock_prices[a - 1:b])

def min_price(a, b):
    return min(stock_prices[a - 1:b])

# Tests
print(f"Price on day 3: {price_at(3)}")
print(f"Max price (days 1-5): {max_price(1, 5)}")
print(f"Min price (days 5-10): {min_price(5, 10)}")
```



## 06. Checkpoint Project: Drive-Thru

Integrating functions, user input, conditional structures, and returned values into a single program.


```python
# Exercise 33: Drive-Thru
def welcome():
    print("Welcome to Fast Food Drive-Thru!")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")

def get_item(x):
    if x == 1:
        return 'Cheeseburger'
    elif x == 2:
        return 'Fries'
    elif x == 3:
        return 'Soda'
    elif x == 4:
        return 'Ice Cream'
    elif x == 5:
        return 'Cookie'
    else:
        return 'Invalid item'

# Execution flow
welcome()
option = int(input('What would you like to order? '))
print(f"You ordered: {get_item(option)}")
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
def double(x):
    return x * 2
```


**Lambda Equivalent:**


```python
double = lambda x: x * 2

print(double(4)) # Output: 8
```


### Common Use Cases: `map()` & `filter()`

Lambda functions shine when passed as one-time arguments to high-order functions like `map()` or `filter()`.


```python
numbers = [1, 2, 3, 4, 5]

# Using map() to multiply each element by 3
tripled_numbers = list(map(lambda x: x * 3, numbers))

# Using filter() to keep only odd numbers
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

print(tripled_numbers) # Output: [3, 6, 9, 12, 15]
print(odd_numbers)     # Output: [1, 3, 5]
```


### Practical Examples

**1. Filtering Text Data:**


```python
names = ['Anthony', 'Benedict', 'Colin', 'Daphne', 'Eloise']

# Filter out names starting with 'A'
filtered_names = list(filter(lambda name: name[0].upper() != 'A', names))

print(filtered_names) # Output: ['Benedict', 'Colin', 'Daphne', 'Eloise']
```


**2. Using Multiple Arguments:**


```python
compound_word = lambda str1, str2: str1 + str2

word = compound_word('fire', 'fly')
print(f'The compound word is: {word}') # Output: The compound word is: firefly
```



