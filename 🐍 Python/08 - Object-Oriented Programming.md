


# 08. Object-Oriented Programming (OOP)

**Course:** Python
**Topic:** Object-Oriented Programming (OOP), Classes, Objects & Instances, Constructor Method (__init__), Instance Methods
**Tags:** `#python` `#oop` `#classes` `#objects` `#data-structures`


Object-Oriented Programming (OOP) allows us to model real-world entities by structuring code into reusable templates called **Classes** and creating concrete instances called **Objects**.

---


## 01. Classes (`class`)

A **Class** serves as a blueprint for defining the structure and behaviors that objects created from it will possess.

By convention in Python, class names use **PascalCase** (capitalizing the first letter of each word).


### Basic Syntax with Default Values

```python
class Guild:
    name = ''
    faction = ''
    level = 0
    is_recruiting = False
```



## 02. Objects & Instance Creation

An **Object** is a concrete instance of a class. Attributes can be accessed and modified individually using dot notation (`.`).


```python
# Instance creation
iron_brothers = Guild()

# Manual attribute assignment
iron_brothers.name = 'The Iron Brothers'
iron_brothers.faction = 'Vanguard Clan'
iron_brothers.level = 42
iron_brothers.is_recruiting = False

# Inspecting object attributes using vars()
print(vars(iron_brothers))
# Output: {'name': 'The Iron Brothers', 'faction': 'Vanguard Clan', 'level': 42, 'is_recruiting': False}
```

> [!TIP] `vars()` Function The built-in `vars(object)` function returns a dictionary containing all attributes assigned to that specific instance.



## 03. The `__init__()` Constructor Method

Assigning attributes line by line is tedious and inefficient. The `__init__()` constructor method runs automatically when instantiating a class, allowing attributes to be initialized dynamically upon creation.


```python
class Dungeon:
    def __init__(self, name, region, difficulty, monsters):
        self.name = name
        self.region = region
        self.difficulty = difficulty
        self.monsters = monsters

# Direct instantiation with arguments
hometown = Dungeon('Sunken Keep', 'Kingdom of Emberfall', 'Hard', ['Gloom Wraith', 'Frost Golem'])
destination = Dungeon('Crystal Spire', 'Sky Realm', 'Nightmare', ['Chrono Warden', 'Void Reaper', 'Star Devourer'])

print(vars(hometown))
print(vars(destination))
```

> [!IMPORTANT] The `self` Parameter The `self` parameter refers implicitly to the current instance of the object being created or manipulated. It must always be the first parameter in methods defined inside a class.


---


## 04. Instance Methods


**Instance Methods** are functions defined inside a class that operate on instances of that class. They can read or modify the object's attributes and must always take `self` as their first parameter.


```python
class Hero:
    def __init__(self, name, level, in_party, power):
        self.name = name
        self.level = level
        self.in_party = in_party
        self.power = power

    def display_info(self):
        print(f"The hero {self.name}'s power rating is {self.power}!")

    def unlock_endgame(self):
        if self.in_party and self.power > 25 and self.level == 12:
            print(f"{self.name} can enter the endgame content!")

# Creating instances and calling methods
aria = Hero('Aria', 11, False, 30)
kai = Hero('Kai', 12, True, 28)

aria.display_info()
kai.unlock_endgame()
```



## 05. Exercise: Player Inventory (`player_inventory.py`)

Implementation of a simple inventory class managing gold state through instance methods.


```python
class PlayerInventory:
    def __init__(self, first_name, last_name, player_id, character_class, pin, gold):
        self.first_name = first_name
        self.last_name = last_name
        self.player_id = player_id
        self.character_class = character_class
        self.pin = pin
        self.gold = gold

    def collect_gold(self, amount):
        self.gold += amount
        return self.gold

    def spend_gold(self, amount):
        self.gold -= amount
        return amount

    def display_gold(self):
        print(f"Current gold: {self.gold} 🪙")

# Test Operations
player = PlayerInventory('Aria', 'Stormborn', 654321, 'Ranger', 4321, 100.0)
player.collect_gold(96)
player.spend_gold(25)
player.display_gold()
```



## 06. Final Project: Bestiary (`bestiary.py`)

A comprehensive model representing bestiary entries using attributes, status checks, and formatted output methods.


```python
class Enemy:
    def __init__(self, entry, name, types, description, is_defeated):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_defeated = is_defeated

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
        
        if self.is_defeated:
            print(f"{self.name} has already been defeated!")
        else:
            print(f"{self.name} has not been defeated yet.")

# Creating bestiary instances
ember_knight = Enemy(25, 'Ember Knight', ['Fire'], 'Its armor smolders when it swings its blade.', True)
frost_wraith = Enemy(1, 'Frost Wraith', ['Ice', 'Dark'], 'It leaves a cold trail wherever it drifts.', True)
stone_golem = Enemy(4, 'Stone Golem', ['Earth'], 'It has a preference for heavy things.', False)

# Testing methods
ember_knight.speak()
ember_knight.display_details()

print()
frost_wraith.speak()
frost_wraith.display_details()
```
