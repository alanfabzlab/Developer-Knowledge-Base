
# 02. Algorithms & Algorithmic Efficiency


## 1. What is an Algorithm?

An **algorithm** is a step-by-step procedure that takes an input, processes it through structured steps, and produces an expected output.

### Examples of Real-World Algorithms
- **Recommendation Systems (e.g., TikTok, Instagram):** Takes user activity (watch time, likes) as input and outputs predicted content.
- **Shortest Path Algorithms (e.g., Google Maps):** Takes start/end locations and traffic conditions as input to compute the quickest route.
- **Sorting Algorithms:** Takes an unordered collection of items and arranges them in alphabetical or numerical order.

---

## 2. Insertion Sort Implementation

Insertion sort is a simple comparison-based sorting algorithm.

Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

input_list = [5, 3, 8, 4, 2, 10]
print(insertion_sort(input_list))
# Output: [2, 3, 4, 5, 8, 10]
````


## 3. Algorithmic Efficiency & Worst-Case Scenario

When designing algorithms, **efficiency** is just as important as correctness. Instead of measuring execution time (which varies by hardware), efficiency is evaluated by calculating how many steps an algorithm takes as the input size grows.


### Comparing Search Strategies

1. **Linear Search:** Checks items one by one sequentially. In the worst case, it can take up to $N$ steps.
    
2. **Binary Search:** Divides the sorted search range in half each step. In the worst case for 100 items, it takes no more than 7 guesses ($\log_2 N$).
    


Python

```python
import random

# Linear Search: O(N) worst-case
def linear_search(arr, target):
    guesses = 0
    for i in range(len(arr)):
        guesses += 1
        if arr[i] == target:
            print(f"Found {target} in {guesses} guesses using linear search.")
            return i
    print(f"{target} not found after {guesses} guesses using linear search.")
    return -1

# Binary Search: O(log N) worst-case
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    guesses = 0
    
    while left <= right:
        guesses += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            print(f"Found {target} in {guesses} guesses using binary search.")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    print(f"{target} not found after {guesses} guesses using binary search.")
    return -1

# Comparison Demo
range_low = 1
range_high = 100000

numbers = [i for i in range(range_low, range_high + 1)]
random_num = random.randint(range_low, range_high)

print(f"Your secret number is {random_num}")
linear_search(numbers, random_num)
binary_search(numbers, random_num)
```


## 4. Practical Application: Amazon Delivery Route Optimization

A classic optimization challenge in Computer Science is route planning (known historically as the **Traveling Salesman Problem**).

- **Data Structure Choice:** A **List** is ideal when execution sequence and order matter.
    
- **Algorithm Goal:** Minimize total distance/time traveled across multiple destination stops.
    


Python

```python
# Delivery route planning using an ordered List
route = [
    "Jersey City (Start)",
    "Ellis Island",
    "Financial District",
    "Lower Manhattan",
    "Brooklyn",
    "Kosciuszko Bridge"
]

print("Planned route:")
for stop in route:
    print(stop)
```