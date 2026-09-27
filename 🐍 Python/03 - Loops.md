---
course: Python
topic: Nested If Statements, while Loops, for Loops & range(), String Interpolation, Rarity Roll
tags:
  - python
  - loops
  - iteration
  - while-loop
  - for-loop
  - logic
---


## Bonus: Nested If Statements

A **nested if statement** is an `if` statement placed inside another `if` statement. Indentation determines the nesting level in Python.

### Syntax & Visual Logic

```python
level = 20
gold = 25000

if level >= 18:
  if gold >= 20000:
    print('You are eligible to buy the legendary blade.')
  else:
    print('Your gold is too low for the legendary blade.')
else:
  print('You must reach level 18 to equip legendary gear.')
```


> **Note:** Avoid nesting conditions deeper than 2-3 levels to maintain code readability.
> 


### Practical Example: Difficulty Decision

```python
difficulty = 'Nightmare'
gear_score = 35

if difficulty == 'Nightmare':
  if gear_score < 60:
    print("You barely survive the dungeon! 💀")
  else:
    print("Even overpowered gear struggles here.")
else:
  print("This difficulty is too easy... let's try a harder one.")
```



## 01. Introduction to Loops & `while` Loops

In programming, a **loop** repeats a block of code until a specific condition is satisfied. Each repetition of a loop is called an **iteration**.


### 🔹 The `while` Loop

A `while` loop continuously executes code inside its block as long as its condition evaluates to `True`.


```python
while condition:
  # code inside executes repeatedly while condition is True
```


### 🏦 Save File Unlock (`unlock_save.py`)

Simulates passcode verification for a locked dungeon gate using a `while` loop:


```python
# unlock_save.py

print('GATE OF THE SUNKEN KEEP')

passcode = int(input('Enter the passcode: '))

while passcode != 2468:
  passcode = int(input('Incorrect passcode. Enter the passcode again: '))

if passcode == 2468:
  print('Gate unlocked!')
```


## 02. Boss HP Guessing Game (`guess.py`)

Demonstrates loop execution control and limiting total attempts using a try counter.

### Basic Guessing Logic


```python
# guess.py (Basic Version)

guess = 0

while guess != 250:
  guess = int(input('Guess the boss HP: '))

print('You got it!')
```



### Guessing Game with Attempt Limits

Incorporating a counter variable `tries` along with logical operators to bound execution:


```python
# guess.py (Limited Attempts Version)

guess = 0
tries = 0

while guess != 250 and tries < 5:
  guess = int(input('Guess the boss HP: '))
  tries += 1

if guess == 250:
  print('You got it!')
else:
  print('Too many attempts! Better luck next time.')
```



## 03. `for` Loops & `range()`

In Python, a **`for` loop** is used to iterate over a sequence (like a list, tuple, or range of numbers). It executes a block of code a specified number of times when paired with the `range()` function.


### 🔹 The `range()` Function
The `range()` function returns a sequence of numbers. By default, it starts at `0` and increments by `1`, ending **one number before** the specified limit.


```python
for i in range(6):
  print(i)
```

**Output:**

```
0
1
2
3
4
5
```

> **Note:** `range(6)` generates numbers from `0` to `5` (6 numbers total). The upper bound is excluded.


### 📝 Grounding Loop (`grinding.py`)

To print a message 100 times using a loop:


```python
# grinding.py

for i in range(100):
  print('I will not skip the boss cutscene')
```



## 04. String Interpolation & `for` Loops (`99_bosses.py`)

### 🔹 String Interpolation (f-strings)

String interpolation substitutes variable values into placeholders within a string using the `f` prefix and curly braces `{}`.


```python
# String Interpolation Example
for i in range(5):
  print(f'The damage of {i} is {i*i}')
```



### 🏹 99 Bosses (`99_bosses.py`)

Prints all verses of the traditional dungeon-crawl chant using a `for` loop, `range()`, and f-strings:


```python
# 99_bosses.py

for i in range(99, 0, -1):
  print(f'{i} skeletons left in the dungeon')
  print(f'{i} skeletons remain')
  print('Slay one down, and the next spawns')
  print(f'{i-1} skeletons left in the dungeon\n')
```



## 05. The Rarity Roll Challenge (`rarity_roll.py`)

A classic challenge that tests conditional logic inside a loot table.

### 📋 Challenge Rules

Loop through numbers from `1` to `100`:

- For multiples of **3**, print `"Common"`.
    
- For multiples of **5**, print `"Rare"`.
    
- For multiples of **both 3 and 5**, print `"Legendary"`.
    
- For all other numbers, print the number itself.
    

### 💡 Implementation


```python
# rarity_roll.py

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('Legendary')
  elif i % 3 == 0:
    print('Common')
  elif i % 5 == 0:
    print('Rare')
  else:
    print(i)
```
