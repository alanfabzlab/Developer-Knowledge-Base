

# 09. Modules

**Course:** Python
**Topic:** Python Modules, Custom Modules (`import`), Built-in `datetime`, Python Packages, Package Management (`pip3`), External Packages (`wikipedia`), The Zen of Python (`import this`)
**Tags:** `#modules` `#random` `#math` `#import`


A **Module** is a Python file (`.py`) containing statements, functions, and class definitions that revolve around a shared purpose. Python comes with over 200 built-in modules (e.g., `random`, `math`, `datetime`).

---


## 01. Importing Modules & Random Choices

The `import` keyword allows access to external or built-in modules.

* `.choices(sequence, k=N)`: Returns a list of `k` randomly selected items from a sequence (items can be selected more than once).

```python
import random

rewards = ['Gold', 'Potion', 'Sword', 'Shield', 'Rune', 'Key']

# Select 3 random items from the list
results = random.choices(rewards, k=3)
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



## 03. Exercise: Loot Box Simulator (`loot_box.py`)

Simulates a gacha loot box selecting three random rarity symbols using `random.choices()`.


```python
import random

symbols = ['⚔️', '💎', '🍀', '🏆']

# Get 3 random symbols
results = random.choices(symbols, k=3)

# Display formatted result
print(f'{results[0]} | {results[1]} | {results[2]}')

# Check win condition
if results == ['🏆', '🏆', '🏆']:
    print('Jackpot! 🏆')
else:
    print('Thanks for playing!')
```



## 04. Exercise: Orbital Moons (`moons.py`)

Calculates the surface area of a randomly selected moon using `pi` from the `math` module and an aliased `choice` function from `random`.

Formula for surface area of a sphere:

$$area = 4 \pi r^2$$


```python
from math import pi
from random import choice as ch

moons = ['Luna', 'Titan', 'Europa', 'Ganymede', 'Io']

# Randomly select a moon
random_moon = ch(moons)

# Determine radius based on selected moon
if random_moon == 'Luna':
    r = 1737
elif random_moon == 'Titan':
    r = 2574
elif random_moon == 'Europa':
    r = 1560
elif random_moon == 'Ganymede':
    r = 2634
elif random_moon == 'Io':
    r = 1821
else:
    print('Oops! An error occurred.')

# Calculate surface area
area = 4 * pi * (r ** 2)

# Print result
print(f'{random_moon} area: {round(area, 2)} sq km')
```


---


## 05. Creating Custom Modules

Modules are `.py` files containing statements, functions, and variables. Any Python file created in a project can be imported into another file within the same directory using the `import` keyword.

```python
# combat_math.py
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
import combat_math
import datetime

combat_math.add(12, 8)       # 20
combat_math.subtract(12, 8)  # 4
combat_math.multiply(12, 8)  # 96
combat_math.divide(12, 8)    # 1.5
combat_math.exp(2, 5)        # 32
```



## 06. Exercise: Countdown (`raid_messages.py` & `main.py`)

Calculates the remaining days until the raid release using custom module imports and the built-in `datetime` module.


```python
# raid_messages.py
import random

raid_messages = [
    'The gates open at dawn. Sharpen your blade! ⚔️',
    "The raid launches at midnight - don't be late! 🕛",
    'The whole server is waiting on you - bring potions! 👏',
    'Have a glorious first clear, champion! 🎁',
    'One more wipe before the patch lands! ⚙️'
]

random_message = random.choice(raid_messages)
```


```python
# main.py
import datetime
import raid_messages

today = datetime.date.today()
raid_release = datetime.date(2027, 11, 3)

days_away = (raid_release - today).days

if today == raid_release:
    print(raid_messages.random_message)
else:
    print(f'The raid launches in {days_away} days!')
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

result = wikipedia.summary("History of video games", sentences=2)
print(result)
```



## 08. The Zen of Python

Python includes an easter egg featuring 19 guiding principles for writing clean and maintainable code, written by Tim Peters.


```python
import this
```
