
# 01. Introduction to Data Structures & Algorithms


## 1. What are Data Structures & Algorithms?

- **Data Structures:** The way we choose to organize and store data efficiently in memory.
- **Algorithms:** A step-by-step procedure or set of rules to solve a specific problem using a data structure.


### Why are DSA Important?
- **Problem-Solving:** Trains structured thinking and pattern recognition to break complex problems into manageable steps.
- **Scalability:** Ensures software efficiently handles large amounts of data as systems scale.
- **Technical Interviews & Real-World Use:** Essential for technical hiring and real-world systems (e.g., NPC pathfinding, loot table resolution, skill-based matchmaking).

---


## 2. Built-in Python Data Structures

### Lists
Ordered collections that allow adding, removing, and accessing elements by index `[]`.

Python

```python
dungeon_map = ['Ashwood', 'Brightfalls', 'Cinderpeak', 'Duskmoor', 'Frostgate']
dungeon_map.append('Goldspan')
print(dungeon_map[2])  # Output: Cinderpeak
```


### Dictionaries

Key-value pair collections allowing efficient lookup by unique keys `{}`.

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


### Sets

Unordered collections of unique elements with no duplicates `{}`.

Python

```python
bosses = {'ember_knight', 'frost_wraith', 'stone_golem'}
bosses.add('void_reaper')
print('ember_knight' in bosses)  # Output: True
```


## 3. Code Example: Sorting and Collections

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
