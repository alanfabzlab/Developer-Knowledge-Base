

# 01. Introduction to Data Structures & Algorithms


## 1. What are Data Structures & Algorithms?

- **Data Structures:** The way we choose to organize and store data efficiently in memory.
- **Algorithms:** A step-by-step procedure or set of rules to solve a specific problem using a data structure.


### Why are DSA Important?
- **Problem-Solving:** Trains structured thinking and pattern recognition to break complex problems into manageable steps.
- **Scalability:** Ensures software efficiently handles large amounts of data as systems scale.
- **Technical Interviews & Real-World Use:** Essential for technical hiring and real-world systems (e.g., search engines, recommendation systems, route optimization).


---


## 2. Built-in Python Data Structures

### Lists
Ordered collections that allow adding, removing, and accessing elements by index `[]`.

Python

```python
cafe_menu = ['Coffee', 'Espresso', 'Cappuccino', 'Latte', 'Tea']
cafe_menu.append('Bubble Tea')
print(cafe_menu[2])  # Output: Cappuccino
````


### Dictionaries

Key-value pair collections allowing efficient lookup by unique keys `{}`.

Python

```python
book = {
    'title': 'The Song of Achilles',
    'author': 'Madeline Miller',
    'genre': 'Historical Fiction',
    'year': 2011
}
print(book['title'])  # Output: The Song of Achilles
```


### Sets

Unordered collections of unique elements with no duplicates `{}`.

Python

```python
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print('apple' in fruits)  # Output: True
```


## 3. Code Example: Sorting and Collections

Python

```python
# Working with built-in data structures
friends = ['Alex', 'Sara', 'Michael']

song = {
    'name': 'Midnight City',
    'artist': 'M83',
    'year': 2011
}

places = {'Tokyo', 'Paris', 'New York'}

# Sorting a list alphabetically using built-in algorithm
concepts = ['queues', 'graphs', 'stacks', 'recursion', "dijkstra's algorithm"]
concepts.sort()
print(concepts)
```