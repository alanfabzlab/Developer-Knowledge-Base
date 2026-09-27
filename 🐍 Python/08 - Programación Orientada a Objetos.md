



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
    nombre = ''
    faccion = ''
    nivel = 0
    reclutando = False
```



## 02. Objetos y Creación de Instancias

Un **Objeto** es una instancia concreta de una clase. Los atributos se pueden acceder y modificar individualmente usando la notación de punto (`.`).


```python
# Creación de la instancia
hermanos_hierro = Guild()

# Asignación manual de atributos
hermanos_hierro.nombre = 'Los Hermanos de Hierro'
hermanos_hierro.faccion = 'Clan de la Vanguardia'
hermanos_hierro.nivel = 42
hermanos_hierro.reclutando = False

# Inspeccionando los atributos del objeto usando vars()
print(vars(hermanos_hierro))
# Salida: {'nombre': 'Los Hermanos de Hierro', 'faccion': 'Clan de la Vanguardia', 'nivel': 42, 'reclutando': False}
```

**Consejo:** Función `vars()` La función integrada `vars(object)` devuelve un diccionario con todos los atributos asignados a esa instancia concreta.



## 03. El Método Constructor `__init__()`

Asignar atributos línea a línea es tedioso e ineficiente. El método constructor `__init__()` se ejecuta automáticamente al instanciar una clase, lo que permite inicializar los atributos de forma dinámica en el momento de la creación.


```python
class Dungeon:
    def __init__(self, nombre, region, dificultad, monstruos):
        self.nombre = nombre
        self.region = region
        self.dificultad = dificultad
        self.monstruos = monstruos

# Instanciación directa con argumentos
ciudad_natal = Dungeon('Fortaleza Hundida', 'Reino de la Caída de Brasa', 'Difícil', ['Espectro Sombrio', 'Golem de Escarcha'])
destino = Dungeon('Aguja de Cristal', 'Reino del Cielo', 'Pesadilla', ['Guardián del Tiempo', 'Segador del Vacio', 'Devorador de Estrellas'])

print(vars(ciudad_natal))
print(vars(destino))
```

**Importante:** El Parámetro `self` El parámetro `self` se refiere implícitamente a la instancia actual del objeto que se está creando o manipulando. Siempre debe ser el primer parámetro en los métodos definidos dentro de una clase.


---


## 04. Métodos de Instancia


Los **Métodos de Instancia** son funciones definidas dentro de una clase que operan sobre instancias de esa clase. Pueden leer o modificar los atributos del objeto y siempre deben recibir `self` como su primer parámetro.


```python
class Hero:
    def __init__(self, nombre, nivel, en_grupo, poder):
        self.nombre = nombre
        self.nivel = nivel
        self.en_grupo = en_grupo
        self.poder = poder

    def display_info(self):
        print(f"El héroe {self.nombre} tiene una potencia de {self.poder}!")

    def unlock_endgame(self):
        if self.en_grupo and self.poder > 25 and self.nivel == 12:
            print(f"¡{self.nombre} puede acceder al contenido del endgame!")

# Creando instancias y llamando a métodos
aria = Hero('Aria', 11, False, 30)
kai = Hero('Kai', 12, True, 28)

aria.display_info()
kai.unlock_endgame()
```



## 05. Ejercicio: Inventario del Jugador (`player_inventory.py`)

Implementación de una clase de inventario sencilla que gestiona el estado del oro mediante métodos de instancia.


```python
class PlayerInventory:
    def __init__(self, nombre, apellido, id_jugador, clase_personaje, pin, oro):
        self.nombre = nombre
        self.apellido = apellido
        self.id_jugador = id_jugador
        self.clase_personaje = clase_personaje
        self.pin = pin
        self.oro = oro

    def collect_gold(self, cantidad):
        self.oro += cantidad
        return self.oro

    def spend_gold(self, cantidad):
        self.oro -= cantidad
        return cantidad

    def display_gold(self):
        print(f"Oro actual: {self.oro} 🪙")

# Operaciones de prueba
jugador = PlayerInventory('Aria', 'Stormborn', 654321, 'Explorador', 4321, 100.0)
jugador.collect_gold(96)
jugador.spend_gold(25)
jugador.display_gold()
```



## 06. Proyecto Final: Bestiario (`bestiary.py`)

Un modelo completo que representa las entradas de un bestiario usando atributos, comprobaciones de estado y métodos de salida formateada.


```python
class Enemy:
    def __init__(self, entrada, nombre, tipos, descripcion, derrotado):
        self.entrada = entrada
        self.nombre = nombre
        self.tipos = tipos
        self.descripcion = descripcion
        self.derrotado = derrotado

    def speak(self):
        print(f"{self.nombre} {self.nombre}!")

    def display_details(self):
        print(f"Número de Entrada: {self.entrada}")
        print(f"Nombre: {self.nombre}")
        
        # Formateando la lista de tipos
        if isinstance(self.tipos, list):
            print(f"Tipo: {', '.join(self.tipos)}")
        else:
            print(f"Tipo: {self.tipos}")

        print(f"Descripción: {self.descripcion}")
        
        if self.derrotado:
            print(f"{self.nombre} ¡ya ha sido derrotado!")
        else:
            print(f"{self.nombre} aún no ha sido derrotado.")

# Creando instancias del bestiario
caballero_brasa = Enemy(25, 'Caballero de Brasa', ['Fuego'], 'Su armadura humea cuando blande su hoja.', True)
espectro_escarcha = Enemy(1, 'Espectro de Escarcha', ['Hielo', 'Oscuro'], 'Deja un rastro frío por donde sea que se deslice.', True)
golem_piedra = Enemy(4, 'Golem de Piedra', ['Tierra'], 'Tiene preferencia por las cosas pesadas.', False)

# Probando métodos
caballero_brasa.speak()
caballero_brasa.display_details()

print()
espectro_escarcha.speak()
espectro_escarcha.display_details()
```
