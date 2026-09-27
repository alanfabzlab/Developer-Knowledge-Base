
<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 🔀 Python Control Flow & Error Handling

![Status Badge](https://img.shields.io/badge/Topic-Control%20Flow-orange?style=for-the-badge)

> [!INFO] Metadata
> **Course:** Python
> **Topic:** Common Errors, Conditional Statements, Relational & Logical Operators
> **Tags:** `#python` `#control-flow` `#logic` `#fundamentals`


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
print(Welcome to the Kingdom!

# SyntaxError: invalid syntax
```

#### ❌ NameError Example

```python
# Error: Referencing an undefined variable
print(goblin_hp)

# NameError: name 'goblin_hp' is not defined

# Fix: Define the variable before referencing it
goblin_hp = 40
print(goblin_hp)  # Output: 40
```

#### ❌ TypeError Example

```python
# Error: Attempting string concatenation with an integer directly
status = 'Player Level: '
print(status + 5)

# TypeError: can only concatenate str (not "int") to str

# Fix: Cast integer using str()
status = 'Player Level: '
print(status + str(5))  # Output: Player Level: 5
```

🐛 Bug Catcher Debugging Challenge (`bug_catcher.py`)

```python
# Fixed version of loot tracking script
health_potions = 5
mana_potions = 8
bomb_runes = 12

print('Loot Bag: ' + str(health_potions) + ' Health Potions')
print('Loot Bag: ' + str(mana_potions) + ' Mana Potions')
print('Loot Bag: ' + str(bomb_runes) + ' Bomb Runes')

total_items = health_potions + mana_potions + bomb_runes
print('Total items: ' + str(total_items) + ' items collected!')
```

## 02. Control Flow & Decision Making

By default, Python runs code sequentially line by line. **Control Flow** allows programs to execute different code blocks depending on specific conditions.

> [!NOTE] Concept Think of control flow as a crossroads: if a condition evaluates to `True`, the program takes one path; if `False`, it takes another.


### 🎲 Damage Roll Simulation (`damage_roll.py`)

Using the `random` module to execute conditional code blocks based on a generated number:

```python
# damage_roll.py
import random

# Generate a random integer between 1 and 6 (a d6 roll)
num = random.randint(1, 6)

if num > 3:
  print('Critical Hit! ⚔️')
else:
  print('Normal Hit 🛡️')
```


## 03. Conditional Statements: `if` & `else`

### 🔹 `if` Statement

Evaluates a condition. If the condition is `True`, the indented block underneath runs.

```python
xp = 75

if xp >= 60:
  print('Level Up Available! ✅')
```


### 🔹 `else` Clause

Provides an alternative execution block when the `if` condition evaluates to `False`.

```python
xp = 45

if xp >= 60:
  print('Level Up Available! ✅')
else:
  print('Not Enough XP Yet ❌')
```


### 🏆 Rank Threshold Checker (`ranks.py`)

Checks whether a match score meets the minimum threshold to unlock the ranked queue (55):

```python
# ranks.py

# Match score (Range 0-100)
score = 78

if score >= 55:
  print('Ranked queue unlocked!')
else:
  print('Keep grinding the campaign.')
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
rarity = 4.8

if rarity >= 4.5:
  print('Mythic Weapon 🌟')
elif rarity >= 3.5:
  print('Legendary Weapon 👍')
elif rarity >= 2.5:
  print('Rare Weapon 😐')
else:
  print('Common Junk 👎')
```


### 🧪 Potion Purity Analysis (`potion_purity.py`)

Checks elixir purity levels to determine how overpowered a brew is:

```python
# potion_purity.py

purity = float(input('Enter purity level (0-100): '))

if purity > 70:
  print('Overpowered')
elif purity < 30:
  print('Sludge')
else:
  print('Balanced')
```


## 05. Generating Random Values (`loot_box.py`)

Python's built-in `random` module provides functions like `randint(a, b)` to produce random integers within a range $[a, b]$ inclusive.

```python
import random

# Generate a result between 1 and 9
option = random.randint(1, 9)

prompt = input('Ask a decision question: ')

if option == 1:
  answer = 'Legendary blade dropped. Definitely.'
elif option == 2:
  answer = 'It is a crit. Decidedly so.'
elif option == 3:
  answer = 'Without a doubt, it crits.'
elif option == 4:
  answer = 'Reroll pending, try again.'
elif option == 5:
  answer = 'Ask again after the patch notes.'
elif option == 6:
  answer = 'Better not tell you now.'
elif option == 7:
  answer = 'My patch notes say no.'
elif option == 8:
  answer = 'DPS check not so good.'
else:
  answer = 'Very doubtful, disconnected.'

print('Question: ' + prompt)
print('Loot Box Oracle: ' + answer)
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
stamina = 8
aim = 6

if stamina > 5 and aim > 5:
  print('Perfect headshot window!')

has_potion = True
has_ether = False

if has_potion or has_ether:
  print('Buffs acquired ☕')

is_paused = False

if not is_paused:
  print('Ready to grind the boss!')
```



### 🎢 Boss Rush Access Checker (`boss_rush.py`)

Evaluates level requirement (Level $40$) and entry tokens ($15\text{ tokens}$):

```python
# boss_rush.py

level = int(input('Enter your level: '))
tokens = int(input('Enter your available tokens: '))

if level >= 40 and tokens >= 15:
  print('Boss Rush unlocked!')
elif tokens >= 15 and level < 40:
  print('You are not high enough level to enter.')
elif level >= 40 and tokens < 15:
  print("You don't have enough tokens.")
else:
  print('Requirements not met for entry.')
```


## 7. Capstone Project: Playstyle Sorting Quiz (`playstyle_quiz.py`)

```python
# playstyle_quiz.py

vanguard = 0
ranger = 0
arcanist = 0
shadow = 0

print('Q1) Do you prefer the frontlines or the backline?')
print('  1) Frontlines')
print('  2) Backline')
q1_answer = int(input('Answer (1-2): '))

if q1_answer == 1:
  vanguard += 1
  arcanist += 1
elif q1_answer == 2:
  ranger += 1
  shadow += 1
else:
  print('Invalid input.')

print('\nQ2) In a party, I want to be remembered as:')
print('  1) The Protector')
print('  2) The Duelist')
print('  3) The Scholar')
print('  4) The Hunter')
q2_answer = int(input('Answer (1-4): '))

if q2_answer == 1:
  vanguard += 2
elif q2_answer == 2:
  shadow += 2
elif q2_answer == 3:
  arcanist += 2
elif q2_answer == 4:
  ranger += 2
else:
  print('Invalid input.')

print('\nQ3) Which soundtrack gets you focused while grinding?')
print('  1) Orchestral Score')
print('  2) Heavy Metal')
print('  3) Lo-Fi Beats')
print('  4) Drum & Bass')
q3_answer = int(input('Answer (1-4): '))

if q3_answer == 1:
  arcanist += 4
elif q3_answer == 2:
  vanguard += 4
elif q3_answer == 3:
  ranger += 4
elif q3_answer == 4:
  shadow += 4
else:
  print('Invalid input.')

print('\n--- Final Scores ---')
print('Vanguard:', vanguard)
print('Ranger:', ranger)
print('Arcanist:', arcanist)
print('Shadow:', shadow)
```
