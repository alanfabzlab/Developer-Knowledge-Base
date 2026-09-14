---
tags:
  - python
  - programming
  - basics
  - open-source
  - notes
status: completed
type: lesson
---

# 🐍 Python Basics: Setup, Output & Data Types

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status Badge](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)

---

## 01. Setting Up & History

> [!INFO] Key Information
> **Python** was created by **Guido van Rossum** in the early 1990s. It is designed to be readable, high-level, and versatile.

### Common Use Cases
- 📊 Data Analysis & Visualization
- 🤖 Artificial Intelligence (AI) & Machine Learning (ML)
- 🌐 Web Development
- 🕹️ Game Development & Scripting

### Core Tools
- **Files:** Code is stored in text files with the `.py` extension.
- **Code Editor:** Software used to write, edit, and run code.

---

## 02. Output & Console Printing

In Python, we use the built-in `print()` function to send text or data to the terminal (output).

```python

# Basic Output
print('Hello World!')

```

> [!TIP] Execution Order
> Python executes code line by line, sequentially from top to bottom.

Python

```python
print('☀️ Morning Dharma!')
print('🦉 Evening Sonny!')

**Output:**

☀️ Morning Dharma!
🦉 Evening Sonny!
```


## 03. Practice Challenges & Patterns

### 📐 Pattern Printing Challenge (`pattern.py`)

To output formatted shapes or text lines, stack multiple `print()` statements:

Python

```python
# pattern.py
print('   1')
print('  2 3')
print(' 4 5 6')
print('7 8 9 10')
```

### 🅰️ Block Letters Challenge (`initials.py`)

Create ASCII block initials accompanied by a code comment.


```python
# Fun fact: Building interactive open-source learning guides!

print("DDDD   L    ")
print("D   D  L    ")
print("D   D  L    ")
print("D   D  L    ")
print("DDDD   LLLLL")
```

## 04. Future Self Letter (`letter.py`)

Using comments (`#`) for documentation alongside output statements:


```python
# Goal: Letter to my future developer self
# Date: 2026

print("Date: September 13, 2026")
print("Status: Feeling excited to build interactive projects.")
print("Goal: Master Python for software and immersive tech.")
print("Message: Keep building consistently every single day!")
print("Favorite Emoji: 🚀")
```

## 05. Variables & Data Types

> [!NOTE] What is a Variable?
> 
> A **variable** acts as a named container that holds a data value in memory.
> 
> Assign values using the equal sign (`=`): `variable_name = value`.


```python
# Variable declarations & reassignment
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
xp = 60
verified = True

# Value Reassignment
xp = 70
xp = 80
print(xp)  # Output: 80
```

| Type        | Name            | Description             | Example |
| :--- | :--- | :--- | :--- |
| **String** | `str` | Text wrapped in single or double quotes | `'Hello'`, `"Python"` |
| **Integer** | `int` | Whole numbers (positive, negative, or zero) | `2026`, `-42` |
| **Float** | `float` | Decimal numbers | `0.75`, `3.14159` |
| **Boolean** | `bool` | Logical truth values | `True`, `False` |

---

## 06. Arithmetic Operators

Python includes standard arithmetic operators for performing mathematical calculations:

| Operator | Name | Description | Example | Result |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Addition | Adds two values together | `4 + 3` | `7` |
| `-` | Subtraction | Subtracts one value from another | `4 - 3` | `1` |
| `*` | Multiplication | Multiplies two values | `4 * 3` | `12` |
| `/` | Division | Divides numerator by denominator (returns float) | `4 / 3` | `1.3333...` |
| `%` | Modulo | Returns the remainder of a division | `10 % 3` | `1` |
| `**` | Exponentiation | Raises base to the power of exponent | `2 ** 3` | `8` |

### 🧮 Practical Examples & Formula Challenges

#### 💡 Tip Calculation (`tip.py`)
```python
pizza = 2.99
coke = 0.99

total = pizza + coke
tip = total * 0.2

print(tip)  # Output: 0.796
```

#### ⚖️ Body Mass Index (`bmi.py`)

$$bmi = \frac{mass}{height^2}$$

```python
# bmi.py
mass = 70    # in kilograms
height = 1.75 # in meters

bmi = mass / (height ** 2)
print(bmi)
```

#### 📐 Pythagorean Theorem (`hypotenuse.py`)

$$c = \sqrt{a^2 + b^2}$$

```python
# hypotenuse.py
a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))

c = (a**2 + b**2) ** 0.5
print(c)
```

## 07. User Input & Type Casting

To interact with users, Python provides the built-in `input()` function.

> [!WARNING] Default Input Type `input()` **always** returns the user response as a `str` (String). To perform calculations, cast it using `int()` or `float()`.

### ⌨️ Standard Input

```python
username = input('Enter your name: ')
print(username)
```

🔢 Type Conversion (`int()`)

```python
age = int(input('What is your age? '))
print(age)  # Stored as integer 24, not string "24"
```

## 08. Chapter Recap Challenge: Currency Converter (`currency.py`)

A multi-currency converter program converting Colombian Pesos, Peruvian Soles, and Brazilian Reais to USD:

```python
# currency.py

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

# Exchange rates (Example standard conversion)
usd_from_pesos = pesos * 0.00025
usd_from_soles = soles * 0.27
usd_from_reais = reais * 0.18

total_usd = usd_from_pesos + usd_from_soles + usd_from_reais

print(total_usd)
```

