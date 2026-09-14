

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



