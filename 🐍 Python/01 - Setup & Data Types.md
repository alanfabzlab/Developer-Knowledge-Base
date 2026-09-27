
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🐍 Python Basics: Setup, Output & Data Types

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)![Status Badge](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)


> [!INFO] Metadata
> **Course:** Python
> **Topic:** Environment Setup, Output, Variables, Data Types & Arithmetic Operators
> **Tags:** `#python` `#programming` `#basics` `#open-source` `#notes`


---

## 01. Setting Up & History

> [!INFO] Key Information
> **Python** was created by **Guido van Rossum** in the early 1990s. It is designed to be readable, high-level, and versatile.

### Common Use Cases
- 🎮 Game Development & Engine Scripting
- 🤖 Artificial Intelligence (AI) & Machine Learning (ML)
- 📊 Data Analysis & Visualization
- 🌐 Web Development

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
print('👾 Hello Developer!')
print('🚀 Systems Ready!')
```

**Output:**

```
👾 Hello Developer!
🚀 Systems Ready!
```


## 03. Practice Challenges & Patterns

### 📐 Damage Counter Challenge (`damage_board.py`)

To output formatted shapes or text lines, stack multiple `print()` statements:

Python

```python
# damage_board.py
print('   1')
print('  2 3')
print(' 4 5 6')
print('7 8 9 10')
```

### 🎮 Block Letters Challenge (`initials.py`)

Create ASCII block initials accompanied by a code comment.


```python
# Fun fact: My favorite genre is dungeon crawler RPGs!

print(" DDD   DDD ")
print("D   D D   D")
print("D   D D   D")
print("D   D D   D")
print(" DDD   DDD ")
```

## 04. Future Self Letter (`letter.py`)

Using comments (`#`) for documentation alongside output statements:


```python
# Goal: Note to my future game developer self
# Date: 2026

print("Date: September 13, 2026")
print("Status: Building a roguelike dungeon crawler in Obsidian.")
print("Goal: Master software engineering and game development.")
print("Message: Ship one dungeon every single day!")
print("Favorite Emoji: 🎮")
```

## 05. Variables & Data Types

> [!NOTE] What is a Variable?
> 
> A **variable** acts as a named container that holds a data value in memory.
> 
> Assign values using the equal sign (`=`): `variable_name = value`.


```python
# Variable declarations & reassignment
hero_name = 'Aria Stormborn'
save_slot = 2
progress = 0.85
xp = 120
has_map = True

# Value Reassignment
xp = 150
xp = 200
print(xp)  # Output: 200
```

| Type        | Name            | Description             | Example |
| :--- | :--- | :--- | :--- |
| **String** | `str` | Text wrapped in single or double quotes | `'Level 12'`, `"Ranger"` |
| **Integer** | `int` | Whole numbers (positive, negative, or zero) | `2026`, `-42` |
| **Float** | `float` | Decimal numbers | `0.75`, `3.14159` |
| **Boolean** | `bool` | Logical truth values | `True`, `False` |

---

## 06. Arithmetic Operators

Python includes standard arithmetic operators for performing mathematical calculations:

|**Operator**|**Name**|**Description**|**Example**|**Result**|
|---|---|---|---|---|
|`+`|Addition|Adds two values together|`15 + 5`|`20`|
|`-`|Subtraction|Subtracts one value from another|`15 - 5`|`10`|
|`*`|Multiplication|Multiplies two values|`15 * 5`|`75`|
|`/`|Division|Divides numerator by denominator (returns float)|`15 / 5`|`3.0`|
|`%`|Modulo|Returns the remainder of a division|`15 % 4`|`3`|
|`**`|Exponentiation|Raises base to the power of exponent|`3 ** 3`|`27`|


### 🧮 Practical Examples & Formula Challenges


#### 💡 Critical Damage Calculation (`crit.py`)
```python
base_damage = 45
weapon_bonus = 15

total = base_damage + weapon_bonus
crit_damage = total * 0.25

print(crit_damage)  # Output: 15.0
```


#### ⚖️ Carry Weight Ratio (`encumbrance.py`)

$$bmi = \frac{mass}{height^2}$$

```python
# encumbrance.py
carry_weight = 80     # in kilograms of carried loot
hero_height = 1.86    # in meters

encumbrance = carry_weight / (hero_height ** 2)
print(encumbrance)
```


#### 📐 Spell Trajectory (`spell_range.py`)

$$c = \sqrt{a^2 + b^2}$$

```python
# spell_range.py
a = int(input('Enter the horizontal cast distance a: '))
b = int(input('Enter the vertical cast distance b: '))

c = (a**2 + b**2) ** 0.5
print(c)
```


## 07. User Input & Type Casting

To interact with users, Python provides the built-in `input()` function.

> [!WARNING] Default Input Type `input()` **always** returns the user response as a `str` (String). To perform calculations, cast it using `int()` or `float()`.
> 


### ⌨️ Standard Input

```python
hero = input('Enter your hero name: ')
print(hero)
```


🔢 Type Conversion (`int()`)

```python
level = int(input('What is your current level? '))
print(level)  # Stored as integer 30, not string "30"
```


## 08. Chapter Recap Challenge: In-Gold Converter (`gold_converter.py`)

A multi-currency converter program converting Copper Coins, Silver Coins, and Emeralds to Gold:

```python
# gold_converter.py

copper = int(input('Amount in copper coins: '))
silver = int(input('Amount in silver coins: '))
emeralds = int(input('Amount of emeralds: '))

# Standard exchange rate factors
gold_from_copper = copper * 0.0001
gold_from_silver = silver * 0.1
gold_from_emeralds = emeralds * 5

total_gold = gold_from_copper + gold_from_silver + gold_from_emeralds

print(total_gold)
```
