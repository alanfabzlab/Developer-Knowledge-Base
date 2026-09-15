---
type: note
course: Codedex Python
chapter: Modules
topic: Modules, Random Choices & Solar System Calculations
tags:
  - python
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
