
# 03. Lists & Linear Search


## 1. Quick Recap: Python Lists

A **List** is an ordered collection of items stored in a single variable. Items are enclosed in square brackets `[]` and separated by commas.

### Indexing and Slicing
- **Indexing:** Access individual items using zero-based indices.
- **Slicing:** Extract sub-segments using `list[start:end]`, where `start` is inclusive and `end` is exclusive.

Python

```python
loot_bag = ['Health Potion', 'Iron Sword', 'Bomb Rune', 'Teleport Scroll', 'Golden Key', 'Monster Pelt']

# Indexing
print(loot_bag[0])  # Output: Health Potion
print(loot_bag[2])  # Output: Bomb Rune

# Slicing
zones = ['Ashwood', 'Brightfalls', 'Cinderpeak', 'Duskmoor', 'Everest', 'Frostgate', 'Goldspan']
print(zones[1:4])  # Output: ['Brightfalls', 'Cinderpeak', 'Duskmoor']
```


### Common List Methods

- `.append(item)`: Adds an item to the end of the list.
    
- `.insert(index, item)`: Inserts an item at a specific index.
    
- `.pop(index)`: Removes and returns an item from a specific index (removes the last item if no index is passed).
    
- `len(list)`: Returns the total number of elements in the list.
    


Python

```python
to_do = ['Craft a health potion', 'Explore the Ashwood', 'Level up at the bonfire']

to_do.append('Clear the Sunken Keep')
to_do.insert(2, 'Recruit a party member')
to_do.pop(4)

print(len(to_do))  # Output: 4
```


## 2. Linear Search Algorithm

**Linear Search** is the simplest searching technique. It inspects each element in a collection sequentially from beginning to end until a matching value is found or the end of the list is reached.


### Algorithm Breakdown

1. **Input:** An unordered list of items and a target value.
    
2. **Process:** Loop through every item sequentially. Compare the current item with the target value.
    
3. **Output:** Return `True` if found, or `False` if the loop ends without a match.
    


### Python Implementation


Python

```python
def linear_search(input_list, target_value):
    for item in input_list:
        if item == target_value:
            return True
    return False

guild_roster = [
    'aria@stormborn.gg',
    'kai@vanguard.clan',
    'nyx@arcanist.gg',
    'borin@ranger.gg',
    'dara@shadow.gg',
    'elowen@arcanist.gg',
    'cass@ranger.gg',
    'jorund@vanguard.clan',
    'vex@shadow.gg',
    'rhea@stormborn.gg',
    'soren@ranger.gg',
    'pleaseaddmeplease@gg.gg',
    'lyra@arcanist.gg'
]

print(linear_search(guild_roster, 'nyx@arcanist.gg'))   # Output: True
print(linear_search(guild_roster, 'mark.scout@gg.gg'))  # Output: False
```


## 3. Algorithmic Efficiency

- **Best Case — $O(1)$:** The target element is at the very beginning of the list. The search terminates immediately in 1 step.
    
- **Worst Case — $O(N)$:** The target element is at the very end or not present in the list at all. The algorithm must check every single item ($N$ operations) before concluding.
