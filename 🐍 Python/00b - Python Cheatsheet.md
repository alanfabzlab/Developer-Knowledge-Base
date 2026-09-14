

# Python Cheatsheet

Quick reference for basic Python syntax and core language concepts.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## 🔹 Basic Output & Input

```python
# Output
print('Hello World!')
print(1000)
print(3.14)
print(True)

# Input
username = input('Enter your name: ')
age = int(input('Enter your age: '))
```


## 🔹 Comments

Python

```python
# I'm a comment!

print('Gabby') # I'm also one T.T
```

## 🔹 Variables & Data Types

Python

```python
secret_num = 42         # int
gravity = 9.81          # float
username = '@snoopdogg' # str
earth_is_flat = False   # bool
```

## 🔹 Operators

### Arithmetic Operations


```python
sum = 23 + 18
difference = 30 - 8
product = 10 * 2.5
quotient = 81 / 9
remainder = 76 % 4
exponent = 2 ** 3
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
if grade >= 90:
  print('A')
elif grade >= 80:
  print('B')
elif grade >= 70:
  print('C')
else:
  print('D')
```

## 🔹 Random Number


```python
import random

num = random.randint(1, 9)
```

## 🔹 String Interpolation


```python
print(f'The square of {i} is {i*i}')
```

## 🔹 Loops


```python
# While loop
while coffee < 1:
  print('Tired of Python')

# For loop
for i in range(10):
  print(i)
```







