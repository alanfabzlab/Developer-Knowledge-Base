---
course: Python
topic: Nested If Statements, while Loops, for Loops & range(), String Interpolation, FizzBuzz
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
age = 20
income = 25000

if age >= 18:
  if income >= 20000:
    print('You are eligible for a loan.')
  else:
    print('Your income is too low to be eligible for a loan.')
else:
  print('You are too young to apply for a loan.')
```


> **Note:** Avoid nesting conditions deeper than 2-3 levels to maintain code readability.
> 

### Practical Example: Weather Decision

```python
weather = 'Sunny'
humidity = 35

if weather == 'Sunny':
  if humidity < 60:
    print("Let's go to the beach! 🏖️")
  else:
    print("Hmmm, it's a little humid for a beach day.")
else:
  print("It's not sunny today... let's try for another day.")
```



## 01. Introduction to Loops & `while` Loops

In programming, a **loop** repeats a block of code until a specific condition is satisfied. Each repetition of a loop is called an **iteration**.


### 🔹 The `while` Loop

A `while` loop continuously executes code inside its block as long as its condition evaluates to `True`.


```python
while condition:
  # code inside executes repeatedly while condition is True
```


### 🏦 ATM Verification Demo (`enter_pin.py`)

Simulates PIN verification using a `while` loop:


```python
# enter_pin.py

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
```


## 02. Guessing Game (`guess.py`)

Demonstrates loop execution control and limiting total attempts using a try counter.

### Basic Guessing Logic


```python
# guess.py (Basic Version)

guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))

print('You got it!')
```



### Guessing Game with Attempt Limits

Incorporating a counter variable `tries` along with logical operators to bound execution:


```python
# guess.py (Limited Attempts Version)

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries += 1

if guess == 6:
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


### 📝 Detention Assignment (`detention.py`)

To write a phrase 100 times using a loop:


```python
# detention.py

for i in range(100):
  print('I will not use Snapchat in class')
```



## 04. String Interpolation & `for` Loops (`99_bottles.py`)

### 🔹 String Interpolation (f-strings)

String interpolation substitutes variable values into placeholders within a string using the `f` prefix and curly braces `{}`.


```python
# String Interpolation Example
for i in range(5):
  print(f'The square of {i} is {i*i}')
```



### 🍻 99 Bottles of Beer (`99_bottles.py`)

Prints all verses of the traditional road trip song using a `for` loop, `range()`, and f-strings:


```python
# 99_bottles.py

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall\n')
```



## 05. The Fizz Buzz Challenge (`fizz_buzz.py`)

A classic programming challenge that tests conditional logic inside a loop.


### 📋 Challenge Rules

Loop through numbers from `1` to `100`:

- For multiples of **3**, print `"Fizz"`.
    
- For multiples of **5**, print `"Buzz"`.
    
- For multiples of **both 3 and 5**, print `"FizzBuzz"`.
    
- For all other numbers, print the number itself.
    

### 💡 Implementation


```python
# fizz_buzz.py

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)
```









