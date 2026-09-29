
# 04. Binary Search

**Spanish version:** [04 - Búsqueda Binaria.md](04%20-%20B%C3%BAsqueda%20Binaria.md)

**Course:** Data Structures & Algorithms
**Topic:** Divide and Conquer, Searching Sorted Lists, Iterative & Recursive Search, Edge Cases
**Tags:** `#dsa` `#searching` `#binary-search` `#complexity`



## 1. What is Binary Search?

**Binary Search** is an efficient algorithm for finding an item in a **sorted list**. It works by repeatedly dividing the search interval in half until the target value is found or the sub-list is empty.

> **Key Prerequisite:** The input list **must be sorted** before applying Binary Search.



---


## 2. How Does Binary Search Work?

Instead of checking elements one by one (like Linear Search), Binary Search eliminates half of the remaining elements in each step:

1. Locate the middle element of the list (`mid`).
2. If the middle element equals the target, search is complete.
3. If the target is smaller than the middle element, discard the right half and search the left half.
4. If the target is larger than the middle element, discard the left half and search the right half.
5. Repeat until the target is found or pointers cross (`left > right`).

This is a **divide and conquer** strategy: the problem is split into two halves, only one half can still contain the target, and the remaining work shrinks exponentially.

---

## 3. Python Implementation

### Iterative Approach

Python

```python
def binary_search(input_list, target):
    left = 0
    right = len(input_list) - 1

    while left <= right:
        mid = (left + right) // 2  # Finds the middle index

        if input_list[mid] == target:
            return True  # Target found
        elif target < input_list[mid]:
            right = mid - 1  # Search the left half
        else:
            left = mid + 1  # Search the right half

    return False  # Target not found
```


### Recursive Approach

The same logic expressed by calling itself on the surviving half. A default value cannot reference `input_list`, so `right` is resolved on the first call and then carried over explicitly:

Python

```python
def binary_search_recursive(input_list, target, left=0, right=None):
    if right is None:
        right = len(input_list) - 1

    if left > right:  # Empty interval — the target cannot be here
        return False

    mid = (left + right) // 2

    if input_list[mid] == target:
        return True
    elif target < input_list[mid]:
        return binary_search_recursive(input_list, target, left, mid - 1)
    else:
        return binary_search_recursive(input_list, target, mid + 1, right)
```


### Execution Example

Python

```python
# The zone map is already sorted — that is the prerequisite
zone_map = ['Ashwood', 'Brightfalls', 'Cinderpeak', 'Duskmoor', 'Everest', 'Frostgate', 'Goldspan']

print(binary_search(zone_map, 'Duskmoor'))   # Output: True
print(binary_search(zone_map, 'Moonspire'))  # Output: False
```

The recursive version returns the same answers on the same list:

Python

```python
print(binary_search_recursive(zone_map, 'Duskmoor'))   # Output: True
print(binary_search_recursive(zone_map, 'Moonspire'))  # Output: False
```

Binary Search also works on numeric data. These are the same enemy speeds that Insertion Sort put in order in the previous note:

Python

```python
enemy_speeds = [20, 30, 45, 55, 80, 95]  # Already sorted with insertion_sort()

print(binary_search(enemy_speeds, 55))  # Output: True
print(binary_search(enemy_speeds, 70))  # Output: False
```


### Edge Case Handling

A search never crashes on a boundary value as long as the interval check is `left <= right` and the pointers move by `mid + 1` / `mid - 1`:

Python

```python
# First and last element of the list
print(binary_search(zone_map, 'Ashwood'))   # Output: True
print(binary_search(zone_map, 'Goldspan'))  # Output: True

# Single-element list, hit and miss
print(binary_search(['Frostgate'], 'Frostgate'))  # Output: True
print(binary_search(['Frostgate'], 'Ashwood'))    # Output: False

# Empty list
print(binary_search([], 'Ashwood'))               # Output: False
```


## 4. Algorithmic Efficiency

- **Time Complexity:** $O(\log N)$ — Halving the problem space at each step dramatically reduces total operations compared to $O(N)$ linear search.
    
- **Space Complexity:** $O(1)$ for iterative implementation, $O(\log N)$ for the recursive one (the call stack holds one frame per halving).

Counting the steps on a 1000-sector map makes the gap measurable:

Python

```python
def binary_search_guesses(input_list, target):
    left, right, guesses = 0, len(input_list) - 1, 0

    while left <= right:
        guesses += 1
        mid = (left + right) // 2

        if input_list[mid] == target:
            return guesses
        elif target < input_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return guesses

def linear_search_guesses(input_list, target):
    for step, item in enumerate(input_list, 1):
        if item == target:
            return step
    return len(input_list)

big_map = [f'Sector-{index:03d}' for index in range(1000)]

print(binary_search_guesses(big_map, 'Sector-000'))  # Output: 9
print(binary_search_guesses(big_map, 'Sector-999'))  # Output: 10
print(linear_search_guesses(big_map, 'Sector-999'))  # Output: 1000
```

Binary Search never needs more than 10 checks over 1000 items, because $2^{10} = 1024$. Linear Search had to walk the entire map.

- **Best Case:** $O(1)$ — the target sits exactly at the first middle index.
    
- **Worst Case:** $O(\log N)$ — the target is absent and every interval is halved until it collapses.



### Common Mistakes

- **Searching an unsorted list:** the algorithm silently returns `False` for values that are present, because the discarded half is no longer guaranteed to hold the wrong side.
    
- **Moving `left = mid` instead of `mid + 1`:** the pointer never advances past `mid` and the loop spins forever.
    
- **Applying it to a linked list:** Binary Search needs $O(1)$ random access, and nodes must be reached one by one.


> **Takeaway:** Sorting is the price paid up front ($O(N \log N)$) in exchange for a search that answers in $O(\log N)$ steps. When a collection is queried over and over, paying once to sort is cheaper than scanning it every time.


