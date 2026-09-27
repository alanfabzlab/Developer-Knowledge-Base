



# 08. Programación Orientada a Objetos (POO)

**Versión original en inglés:** [08 - Object-Oriented Programming.md](./08%20-%20Object-Oriented%20Programming.md)

**Curso:** Python
**Tema:** Programación orientada a objetos (POO), clases, objetos e instancias, método constructor (__init__), métodos de instancia
**Etiquetas:** `#python` `#oop` `#classes` `#objects` `#data-structures`


La Programación Orientada a Objetos (POO) nos permite modelar entidades del mundo real estructurando el código en plantillas reutilizables llamadas **Clases** y creando instancias concretas llamadas **Objetos**.

---


## 01. Clases (`class`)

Una **Clase** sirve como plano para definir la estructura y los comportamientos que tendrán los objetos creados a partir de ella.

Por convención en Python, los nombres de clase usan **PascalCase** (con la primera letra de cada palabra en mayúscula).


### Sintaxis Básica con Valores por Defecto

```python
class Guild:
    name = ''
    faction = ''
    level = 0
    is_recruiting = False
```



## 02. Objetos y Creación de Instancias

Un **Objeto** es una instancia concreta de una clase. Los atributos se pueden acceder y modificar individualmente usando la notación de punto (`.`).


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

**Consejo:** Función `vars()` La función integrada `vars(object)` devuelve un diccionario con todos los atributos asignados a esa instancia concreta.



## 03. El Método Constructor `__init__()`

Asignar atributos línea a línea es tedioso e ineficiente. El método constructor `__init__()` se ejecuta automáticamente al instanciar una clase, lo que permite inicializar los atributos de forma dinámica en el momento de la creación.


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

**Importante:** El Parámetro `self` El parámetro `self` se refiere implícitamente a la instancia actual del objeto que se está creando o manipulando. Siempre debe ser el primer parámetro en los métodos definidos dentro de una clase.


---


## 04. Métodos de Instancia


Los **Métodos de Instancia** son funciones definidas dentro de una clase que operan sobre instancias de esa clase. Pueden leer o modificar los atributos del objeto y siempre deben recibir `self` como su primer parámetro.


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



## 05. Ejercicio: Inventario del Jugador (`player_inventory.py`)

Implementación de una clase de inventario sencilla que gestiona el estado del oro mediante métodos de instancia.


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



## 06. Proyecto Final: Bestiario (`bestiary.py`)

Un modelo completo que representa las entradas de un bestiario usando atributos, comprobaciones de estado y métodos de salida formateada.


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
