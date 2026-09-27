
# 01. Introducción a Estructuras de Datos y Algoritmos

**Versión original en inglés:** [01 - Introduction to DSA.md](01%20-%20Introduction%20to%20DSA.md)

**Curso:** Estructuras de Datos y Algoritmos
**Tema:** Conceptos Fundamentales, Estructuras de Datos Integradas y Resolución de Problemas
**Etiquetas:** `#dsa` `#data-structures` `#fundamentals`



## 1. ¿Qué son las Estructuras de Datos y los Algoritmos?

- **Estructuras de Datos:** La forma en que elegimos organizar y almacenar datos de manera eficiente en memoria.
- **Algoritmos:** Un procedimiento paso a paso o un conjunto de reglas para resolver un problema específico usando una estructura de datos.


### ¿Por qué son importantes las EDD?
- **Resolución de problemas:** Entrena el pensamiento estructurado y el reconocimiento de patrones para dividir problemas complejos en pasos manejables.
- **Escalabilidad:** Asegura que el software maneje eficientemente grandes cantidades de datos a medida que los sistemas escalan.
- **Entrevistas técnicas y uso en el mundo real:** Esenciales para la contratación técnica y los sistemas del mundo real (por ejemplo, búsqueda de rutas de NPC, resolución de tablas de botín, emparejamiento por habilidad).

---


## 2. Estructuras de Datos Integradas de Python

### Listas
Colecciones ordenadas que permiten agregar, eliminar y acceder a elementos por índice `[]`.

Python

```python
dungeon_map = ['Ashwood', 'Brightfalls', 'Cinderpeak', 'Duskmoor', 'Frostgate']
dungeon_map.append('Goldspan')
print(dungeon_map[2])  # Output: Cinderpeak
```


### Diccionarios

Colecciones de pares clave-valor que permiten una búsqueda eficiente mediante claves únicas `{}`.

Python

```python
save_file = {
    'slot': 'Chrono Warden',
    'region': 'Sunken Keep',
    'difficulty': 'Nightmare',
    'playtime': 2041
}
print(save_file['slot'])  # Output: Chrono Warden
```


### Conjuntos

Colecciones no ordenadas de elementos únicos, sin duplicados `{}`.

Python

```python
bosses = {'ember_knight', 'frost_wraith', 'stone_golem'}
bosses.add('void_reaper')
print('ember_knight' in bosses)  # Output: True
```


## 3. Ejemplo de Código: Ordenamiento y Colecciones

Python

```python
# Working with built-in data structures
party = ['Aria', 'Kai', 'Nyx']

boss_theme = {
    'name': 'Final Boss Concerto',
    'composer': 'R. Vale',
    'year': 2011
}

biomes = {'Ashwood', 'Frostgate', 'Goldspan'}

# Sorting a list alphabetically using built-in algorithm
mechanics = ['loot', 'pathfinding', 'queues', 'recursion', "dijkstra's algorithm"]
mechanics.sort()
print(mechanics)
```
