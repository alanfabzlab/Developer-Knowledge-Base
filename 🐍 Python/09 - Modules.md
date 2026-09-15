---
course: Python
topic: Python Modules, Custom Modules (`import`), Built-in `datetime`, Python Packages, Package Management (`pip3`), External Packages (`wikipedia`), The Zen of Python (`import this`)
  - modules
  - random
  - math
  - import
---


# 09. Modules

A **Module** is a Python file (`.py`) containing statements, functions, and class definitions that revolve around a shared purpose. Python comes with over 200 built-in modules (e.g., `random`, `math`, `datetime`).

---


## 01. Importing Modules & Random Choices

The `import` keyword allows access to external or built-in modules.

* `.choices(sequence, k=N)`: Returns a list of `k` randomly selected items from a sequence (items can be selected more than once).

```python
import random

dice = [1, 2, 3, 4, 5, 6]

# Select 3 random items from the list
results = random.choices(dice, k=3)
print(results)
```


## 02. Importing Specific Items & Aliasing

- `from module import object`: Imports specific functions, variables, or classes directly into the local namespace.
    
- `as alias`: Renames an imported module or function with a shorthand alias (aliasing).
    


```python
# Direct import
from random import choice, sample

# Aliasing imported functions
from random import choice as ch
from math import pi
```



## 03. Exercise: Slot Machine (`slot_machine.py`)

Simulates a classic slot machine selecting three random fruit/seven symbols using `random.choices()`.


```python
import random

symbols = ['🎰', '🍇', '🍉', '7️⃣']

# Get 3 random symbols
results = random.choices(symbols, k=3)

# Display formatted result
print(f'{results[0]} | {results[1]} | {results[2]}')

# Check win condition
if results == ['7️⃣', '7️⃣', '7️⃣']:
    print('Jackpot! 💰')
else:
    print('Thanks for playing!')
```



## 04. Exercise: Solar System (`solar_system.py`)

Calculates the surface area of a randomly selected planet using `pi` from the `math` module and an aliased `choice` function from `random`.

Formula for surface area of a sphere:

$$area = 4 \pi r^2$$


```python
from math import pi
from random import choice as ch

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

# Randomly select a planet
random_planet = ch(planets)

# Determine radius based on selected planet
if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print('Oops! An error occurred.')

# Calculate surface area
area = 4 * pi * (r ** 2)

# Print result
print(f'{random_planet} area: {round(area, 2)} sq km')
```


---


## 05. Creating Custom Modules

Modules are `.py` files containing statements, functions, and variables. Any Python file created in a project can be imported into another file within the same directory using the `import` keyword.

```python
# calculator.py
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
```



```python
# main.py
import calculator
import datetime

calculator.add(3, 4)       # 7
calculator.subtract(3, 4)  # -1
calculator.multiply(3, 4)  # 12
calculator.divide(3, 4)    # 0.75
calculator.exp(3, 4)       # 81
```



## 06. Exercise: Countdown (`bday_messages.py` & `main.py`)

Calculates the remaining days until a birthday using custom module imports and the built-in `datetime` module.


```python
# bday_messages.py
import random

bday_messages = [
    'Hope you have a very Happy Birthday! 🎉',
    "It's your special day - get out there and celebrate! 🥳",
    'You were born and the world got better - everybody wins! 👏',
    'Have lots of fun on your special day! 🎁',
    'Another year of you going around the sun! ☀️'
]

random_message = random.choice(bday_messages)
```


```python
# main.py
import datetime
import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2027, 4, 15)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')
```



## 07. Python Packages & `pip3`

- **Package**: A folder containing related modules along with an `__init__.py` file.
    
- **Libraries**: Large, specialized packages designed for broader application development.
    
- **PyPI**: The official Python Package Index containing external open-source packages.
    
- **`pip3`**: The command-line package manager used to install external Python packages.
    


```bash
# Installing third-party packages via terminal
pip3 install wikipedia
```


### Exercise: Wikipedia Query (`wiki.py`)


```python
# wiki.py
import wikipedia

result = wikipedia.summary("Philosophy of life", sentences=2)
print(result)
```


## 08. The Zen of Python

Python includes an easter egg featuring 19 guiding principles for writing clean and maintainable code, written by Tim Peters.


```python
import this
```
