


# Chuleta de Python II

**Versión original en inglés:** [00c - Python Cheatsheet II.md](./00c%20-%20Python%20Cheatsheet%20II.md)

**Curso:** Python
**Tema:** Listas, funciones y métodos de lista, funciones, parámetros, ámbito, clases y objetos, módulos
**Etiquetas:** `#python` `#cheatsheet` `#syntax` `#reference`



---

### Listas

```python
hp_enemigo = [320, 280, 410, 190, 540, 260, 130]

# Index
jefe_1 = hp_enemigo[0]  # 320
jefe_7 = hp_enemigo[6]  # 130

# Negative index
jefe_7 = hp_enemigo[-1] # 130

# Slicing
olas_iniciales = hp_enemigo[0:5]
olas_finales = hp_enemigo[5:7]
```



### Funciones y Métodos de Lista


```python
tiempos_fase = [140, 95, 180, 120]

# Built-in functions
len(tiempos_fase)  # Output: 4
max(tiempos_fase)  # Output: 180
min(tiempos_fase)  # Output: 95

# Built-in methods
tiempos_fase.append(205)
# [140, 95, 180, 120, 205]

tiempos_fase.insert(3, 160)
# [140, 95, 180, 160, 120, 205]

tiempos_fase.remove(95)
# [140, 180, 160, 120, 205]

tiempos_fase.pop(0)
# [180, 160, 120, 205]
```


### Funciones


```python
def announce_wave():
    print('¡Aparece el jefe! 👹')

announce_wave()  # Output: The boss spawns! 👹
```


### Parámetros


```python
def add(x, y):
    return x + y

print(add(2, 3))    # Output: 5
print(add(21, 56))  # Output: 77
```


### Ámbito


```python
experiencia = 29  # Global scope

def func():
    experiencia = 42  # Local scope
    print(experiencia)

print(experiencia)  # Output: 29
func()    # Output: 42
```


### Clases y Objetos


```python
class Hero:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def say_hi(self):
        print(f'👋 Mi nombre es {self.nombre}')

aria = Hero('Aria', 22)
kai = Hero('Kai', 23)

aria.say_hi()  # 👋 My name is Aria
```


### Módulos


```python
import matplotlib.pyplot as plt
import random

print(random.randint(1, 10))

x = [1, 2, 3]
y = [4, 9, 16]

plt.plot(x, y)
plt.show()
```
