

# Python Cheatsheet II

> [!INFO] Metadata
> **Course:** Python
> **Topic:** Lists, List Functions & Methods, Functions, Parameters, Scope, Classes & Objects, Modules
> **Tags:** `#python` `#cheatsheet` `#syntax` `#reference`



---

### Lists

```python
enemy_hp = [320, 280, 410, 190, 540, 260, 130]

# Index
boss_1 = enemy_hp[0]  # 320
boss_7 = enemy_hp[6]  # 130

# Negative index
boss_7 = enemy_hp[-1] # 130

# Slicing
early_waves = enemy_hp[0:5]
late_waves = enemy_hp[5:7]
```



### List Functions & Methods


```python
stage_runtimes = [140, 95, 180, 120]

# Built-in functions
len(stage_runtimes)  # Output: 4
max(stage_runtimes)  # Output: 180
min(stage_runtimes)  # Output: 95

# Built-in methods
stage_runtimes.append(205)
# [140, 95, 180, 120, 205]

stage_runtimes.insert(3, 160)
# [140, 95, 180, 160, 120, 205]

stage_runtimes.remove(95)
# [140, 180, 160, 120, 205]

stage_runtimes.pop(0)
# [180, 160, 120, 205]
```


### Functions


```python
def announce_wave():
    print('The boss spawns! 👹')

announce_wave()  # Output: The boss spawns! 👹
```


### Parameters


```python
def add(x, y):
    return x + y

print(add(2, 3))    # Output: 5
print(add(21, 56))  # Output: 77
```


### Scope


```python
xp = 29  # Global scope

def func():
    xp = 42  # Local scope
    print(xp)

print(xp)  # Output: 29
func()    # Output: 42
```


### Classes & Objects


```python
class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def say_hi(self):
        print(f'👋 My name is {self.name}')

aria = Hero('Aria', 22)
kai = Hero('Kai', 23)

aria.say_hi()  # 👋 My name is Aria
```


### Modules


```python
import matplotlib.pyplot as plt
import random

print(random.randint(1, 10))

x = [1, 2, 3]
y = [4, 9, 16]

plt.plot(x, y)
plt.show()
```
