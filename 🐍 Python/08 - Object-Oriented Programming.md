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


---


## 04. Instance Methods


**Instance Methods** are functions defined inside a class that operate on instances of that class. They can read or modify the object's attributes and must always take `self` as their first parameter.


```python
class Student:
    def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa

    def display_info(self):
        print(f"The student {self.name}'s GPA is {self.gpa}!")

    def graduation(self):
        if self.enrolled and self.gpa > 2.5 and self.year == 12:
            print(f"{self.name} will be able to graduate this year!")

# Creating instances and calling methods
mitsuha = Student('Mitsuha', 11, False, 4.0)
taki = Student('Taki', 12, True, 3.8)

mitsuha.display_info()
taki.graduation()
```



## 05. Exercise: Bank Account (`bank_accounts.py`)

Implementation of a simple bank account class managing balance state through instance methods.


```python
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def display_balance(self):
        print(f"Current balance: ${self.balance}")

# Test Operations
account = BankAccount('Alan', 'Fabricio', 123456, 'Checking', 4321, 100.0)
account.deposit(96)
account.withdraw(25)
account.display_balance()
```



## 06. Final Project: Pokédex (`pokedex.py`)

A comprehensive model representing Pokémon entries using attributes, status checks, and formatted output methods.


```python
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name} {self.name}!")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        
        # Formatting list of types
        if isinstance(self.types, list):
            print(f"Type: {', '.join(self.types)}")
        else:
            print(f"Type: {self.types}")

        print(f"Description: {self.description}")
        
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")

# Creating Pokémon instances
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks.', True)
bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass', 'Poison'], 'There is a plant seed on its back since birth.', True)
charmander = Pokemon(4, 'Charmander', ['Fire'], 'It has a preference for hot things.', False)

# Testing methods
pikachu.speak()
pikachu.display_details()

print()
bulbasaur.speak()
bulbasaur.display_details()
```





