


# 09. Módulos

**Versión original en inglés:** [09 - Modules.md](./09%20-%20Modules.md)

**Curso:** Python
**Tema:** Módulos de Python, módulos personalizados (`import`), módulo integrado `datetime`, paquetes de Python, gestión de paquetes (`pip3`), paquetes externos (`wikipedia`), El Zen de Python (`import this`)
**Etiquetas:** `#modules` `#random` `#math` `#import`


Un **Módulo** es un archivo de Python (`.py`) que contiene sentencias, funciones y definiciones de clases que giran en torno a un propósito compartido. Python viene con más de 200 módulos integrados (por ejemplo, `random`, `math`, `datetime`).

---


## 01. Importando Módulos y Elecciones Aleatorias

La palabra clave `import` permite acceder a módulos externos o integrados.

* `.choices(sequence, k=N)`: Devuelve una lista de `k` elementos seleccionados al azar de una secuencia (los elementos pueden seleccionarse más de una vez).

```python
import random

rewards = ['Gold', 'Potion', 'Sword', 'Shield', 'Rune', 'Key']

# Select 3 random items from the list
results = random.choices(rewards, k=3)
print(results)
```


## 02. Importando Elementos Específicos y Creando Alias

- `from module import object`: Importa funciones, variables o clases específicas directamente en el ámbito local.
    
- `as alias`: Renombra un módulo o función importado con un alias abreviado (aliasing).
    


```python
# Direct import
from random import choice, sample

# Aliasing imported functions
from random import choice as ch
from math import pi
```



## 03. Ejercicio: Simulador de Caja de Botín (`loot_box.py`)

Simula una caja de botín tipo gacha que selecciona tres símbolos de rareza al azar usando `random.choices()`.


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



## 04. Ejercicio: Lunas Orbitales (`moons.py`)

Calcula el área superficial de una luna seleccionada al azar usando `pi` del módulo `math` y una función `choice` con alias de `random`.

Fórmula del área superficial de una esfera:

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


## 05. Creando Módulos Personalizados

Los módulos son archivos `.py` que contienen sentencias, funciones y variables. Cualquier archivo de Python creado en un proyecto se puede importar en otro archivo del mismo directorio usando la palabra clave `import`.

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



## 06. Ejercicio: Cuenta Atrás (`raid_messages.py` y `main.py`)

Calcula los días restantes hasta el lanzamiento de la incursión usando importaciones de módulos personalizados y el módulo integrado `datetime`.


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



## 07. Paquetes de Python y `pip3`

- **Paquete**: Una carpeta que contiene módulos relacionados junto con un archivo `__init__.py`.
    
- **Bibliotecas**: Paquetes grandes y especializados, diseñados para el desarrollo de aplicaciones más amplias.
    
- **PyPI**: El Índice de Paquetes de Python oficial, que contiene paquetes de código abierto externos.
    
- **`pip3`**: El gestor de paquetes de línea de comandos usado para instalar paquetes externos de Python.
    


```bash
# Installing third-party packages via terminal
pip3 install wikipedia
```


### Ejercicio: Consulta a Wikipedia (`wiki.py`)


```python
# wiki.py
import wikipedia

result = wikipedia.summary("History of video games", sentences=2)
print(result)
```



## 08. El Zen de Python

Python incluye un huevo de pascua con 19 principios Rectores para escribir código limpio y mantenible, escritos por Tim Peters.


```python
import this
```
