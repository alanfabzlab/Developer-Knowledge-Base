
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
print('¡Listo Jugador Uno!')
print(1000)
print(3.14)
print(True)

# Input
nombre_heroe = input('Introduce el nombre de tu héroe: ')
nivel = int(input('Introduce tu nivel: '))
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
oro_inicial = 150       # int
gravedad = 9.81          # float
etiqueta_jugador = '@nightowl' # str
juego_terminado = False   # bool
```

## 🔹 Operadores

### Operaciones Aritméticas


```python
daño_recibido = 23 + 18
hp_restante = 30 - 8
prob_crit = 10 * 2.5
tasa_oro = 81 / 9
num_ola = 76 % 4
nivel_botin = 2 ** 3
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
if puntuacion_rango >= 90:
  print('S')
elif puntuacion_rango >= 80:
  print('A')
elif puntuacion_rango >= 70:
  print('B')
else:
  print('C')
```

## 🔹 Número Aleatorio


```python
import random

tirada = random.randint(1, 20)
```

## 🔹 Interpolación de Cadenas


```python
print(f'El daño de {i} es {i*i}')
```

## 🔹 Bucles


```python
# While loop
while vida < 1:
  print('¡Tu vida es crítica!')

# For loop
for i in range(5):
  print(i)
```
