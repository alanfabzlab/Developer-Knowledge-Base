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

Python

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

Python

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

Python

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



