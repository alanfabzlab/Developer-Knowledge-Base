
# 03. Lists & Linear Search


## 1. Quick Recap: Python Lists

A **List** is an ordered collection of items stored in a single variable. Items are enclosed in square brackets `[]` and separated by commas.

### Indexing and Slicing
- **Indexing:** Access individual items using zero-based indices.
- **Slicing:** Extract sub-segments using `list[start:end]`, where `start` is inclusive and `end` is exclusive.

Python

```python
grocery = ['Eggs', 'Avocados', 'Cookies', 'Hot Pepper Jam', 'Blueberries', 'Broccoli']

# Indexing
print(grocery[0])  # Output: Eggs
print(grocery[2])  # Output: Cookies

# Slicing
signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra']
print(signs[1:4])  # Output: ['Taurus', 'Gemini', 'Cancer']
````


### Common List Methods

- `.append(item)`: Adds an item to the end of the list.
    
- `.insert(index, item)`: Inserts an item at a specific index.
    
- `.pop(index)`: Removes and returns an item from a specific index (removes the last item if no index is passed).
    
- `len(list)`: Returns the total number of elements in the list.
    


Python

```python
to_do = ['Put on laundry', 'Take a walk', 'Make some tea']

to_do.append('Complete DSA chapter 2')
to_do.insert(2, 'FaceTime mom')
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

email_list = [
    'dwight.schrute@dundermiffin.com',
    'michael.scott@dundermiffin.com',
    'mgoodyear@lumonindustries.com',
    'walter.white@jpwynnehigh.edu',
    'hank@dea.gov',
    'kimberly.finkle@essexedu.edu',
    'sheldon@caltech.edu',
    'elliot@allsafe.com',
    'mr.robot@fsociety.com',
    'mulder@fbi.gov',
    'carrie@sexandthecity.tvs',
    'pleasecallmebarney@yahoo.com',
    'buffy@sunnydale.edu'
]

print(linear_search(email_list, 'mgoodyear@lumonindustries.com'))  # Output: True
print(linear_search(email_list, 'mark.scout@lumonindustries.com'))     # Output: False
```


## 3. Algorithmic Efficiency

- **Best Case — $O(1)$:** The target element is at the very beginning of the list. The search terminates immediately in 1 step.
    
- **Worst Case — $O(N)$:** The target element is at the very end or not present in the list at all. The algorithm must check every single item ($N$ operations) before concluding.