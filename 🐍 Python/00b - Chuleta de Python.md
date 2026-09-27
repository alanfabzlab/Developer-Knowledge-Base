
# Chuleta de Python

**Versión original en inglés:** [00b - Python Cheatsheet.md](./00b%20-%20Python%20Cheatsheet.md)

**Curso:** Python
**Tema:** Sintaxis, E/S básica, tipos de datos y referencia rápida
**Etiquetas:** `#python` `#cheatsheet` `#syntax` `#basics` `#reference`


Referencia rápida de la sintaxis básica de Python y de los conceptos fundamentales del lenguaje, usando datos de videojuegos como ejemplos a lo largo de la nota.

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## 🔹 Salida y Entrada Básicas

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


## 🔹 Comentarios

Python

```python
# I'm a comment!

print('Aria') # I'm also one T.T
```

## 🔹 Variables y Tipos de Datos

Python

```python
starting_gold = 150       # int
gravity = 9.81          # float
player_tag = '@nightowl' # str
is_game_over = False   # bool
```

## 🔹 Operadores

### Operaciones Aritméticas


```python
damage_taken = 23 + 18
hp_remaining = 30 - 8
crit_chance = 10 * 2.5
gold_rate = 81 / 9
wave_number = 76 % 4
loot_tier = 2 ** 3
```

### Operadores Relacionales


```python
a == b  # Equal to
a != b  # Not equal to
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal to
a <= b  # Less than or equal to
```

### Operadores Lógicos


```python
a and b # True if both are true
a or b  # True if at least one is true
not a   # True if a is false
```

## 🔹 Control de Flujo


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

## 🔹 Número Aleatorio


```python
import random

roll = random.randint(1, 20)
```

## 🔹 Interpolación de Cadenas


```python
print(f'The damage of {i} is {i*i}')
```

## 🔹 Bucles


```python
# While loop
while health < 1:
  print('Your health is critical!')

# For loop
for i in range(5):
  print(i)
```
