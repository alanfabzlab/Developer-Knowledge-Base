
# Python Cheatsheet

> [!INFO] Metadata
> **Course:** Python
> **Topic:** Syntax, Basic I/O, Data Types & Quick Reference
> **Tags:** `#python` `#cheatsheet` `#syntax` `#basics` `#reference`


Quick reference for basic Python syntax and core language concepts, using video game data as running examples.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## 🔹 Basic Output & Input

```python
# Output
print('Ready Player One!')
print(1000)
print(3.14)
print(True)

# Input
hero_name = input('Enter your hero name: ')
level = int(input('Enter your level: '))
```


## 🔹 Comments

Python

```python
# I'm a comment!

print('Aria') # I'm also one T.T
```

## 🔹 Variables & Data Types

Python

```python
starting_gold = 150       # int
gravity = 9.81          # float
player_tag = '@nightowl' # str
is_game_over = False   # bool
```

## 🔹 Operators

### Arithmetic Operations


```python
damage_taken = 23 + 18
hp_remaining = 30 - 8
crit_chance = 10 * 2.5
gold_rate = 81 / 9
wave_number = 76 % 4
loot_tier = 2 ** 3
```

### Relational Operators


```python
a == b  # Equal to
a != b  # Not equal to
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal to
a <= b  # Less than or equal to
```

### Logical Operators


```python
a and b # True if both are true
a or b  # True if at least one is true
not a   # True if a is false
```

## 🔹 Control Flow


```python
if rank_score >= 90:
  print('S')
elif rank_score >= 80:
  print('A')
elif rank_score >= 70:
  print('B')
else:
  print('C')
```

## 🔹 Random Number


```python
import random

roll = random.randint(1, 20)
```

## 🔹 String Interpolation


```python
print(f'The damage of {i} is {i*i}')
```

## 🔹 Loops


```python
# While loop
while health < 1:
  print('Your health is critical!')

# For loop
for i in range(5):
  print(i)
```
