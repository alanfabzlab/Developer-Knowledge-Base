
---
type: note
course: Codedex Python
chapter: Object-Oriented Programming
topic: Classes, Objects & Init Method
tags:
  - python
  - oop
  - classes
  - objects
  - data-structures
---


# 08. Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) allows us to model real-world entities by structuring code into reusable templates called **Classes** and creating concrete instances called **Objects**.

---


## 01. Classes (`class`)

A **Class** serves as a blueprint for defining the structure and behaviors that objects created from it will possess.

By convention in Python, class names use **PascalCase** (capitalizing the first letter of each word).


### Basic Syntax with Default Values

```python
class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False
```



## 02. Objects & Instance Creation

An **Object** is a concrete instance of a class. Attributes can be accessed and modified individually using dot notation (`.`).


```python
# Instance creation
bobs_burgers = Restaurant()

# Manual attribute assignment
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

# Inspecting object attributes using vars()
print(vars(bobs_burgers))
# Output: {'name': "Bob's Burgers", 'category': 'American Diner', 'rating': 4.7, 'delivery': False}
```

> [!TIP] `vars()` Function The built-in `vars(object)` function returns a dictionary containing all attributes assigned to that specific instance.


## 03. The `__init__()` Constructor Method

Assigning attributes line by line is tedious and inefficient. The `__init__()` constructor method runs automatically when instantiating a class, allowing attributes to be initialized dynamically upon creation.


```python
class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

# Direct instantiation with arguments
hometown = City('Mexico City', 'Mexico', 9200000, ['Zocalo', 'Angel de la Independencia'])
destination = City('Tokyo', 'Japan', 14000000, ['Shinjuku', 'Tokyo Tower', 'Senso-ji'])

print(vars(hometown))
print(vars(destination))
```

> [!IMPORTANT] The `self` Parameter The `self` parameter refers implicitly to the current instance of the object being created or manipulated. It must always be the first parameter in methods defined inside a class.




