


# Chuleta de Python II

**Versión original en inglés:** [00c - Python Cheatsheet II.md](./00c%20-%20Python%20Cheatsheet%20II.md)

**Curso:** Python
**Tema:** Listas, funciones y métodos de lista, funciones, parámetros, ámbito, clases y objetos, módulos
**Etiquetas:** `#python` `#cheatsheet` `#syntax` `#reference`



---

### Listas

```python
hp_enemigo = [320, 280, 410, 190, 540, 260, 130]

# Índice
jefe_1 = hp_enemigo[0]  # 320
jefe_7 = hp_enemigo[6]  # 130

# Índice negativo
jefe_7 = hp_enemigo[-1] # 130

# Rebanado
olas_iniciales = hp_enemigo[0:5]
olas_finales = hp_enemigo[5:7]
```



### Funciones y Métodos de Lista


```python
tiempos_fase = [140, 95, 180, 120]

# Funciones integradas
len(tiempos_fase)  # Salida: 4
max(tiempos_fase)  # Salida: 180
min(tiempos_fase)  # Salida: 95

# Métodos integrados
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

announce_wave()  # Salida: ¡Aparece el jefe! 👹
```


### Parámetros


```python
def add(x, y):
    return x + y

print(add(2, 3))    # Salida: 5
print(add(21, 56))  # Salida: 77
```


### Ámbito


```python
experiencia = 29  # Ámbito global

def func():
    experiencia = 42  # Ámbito local
    print(experiencia)

print(experiencia)  # Salida: 29
func()    # Salida: 42
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

aria.say_hi()  # 👋 Mi nombre es Aria
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
