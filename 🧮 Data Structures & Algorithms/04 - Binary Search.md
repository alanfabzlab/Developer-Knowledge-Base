
# 04. Binary Search

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
````


### Execution Example

Python

```python
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

print(binary_search(email_list, 'mgoodyear@lumonindustries.com'))  # Output: True
print(binary_search(email_list, 'mark.scout@lumonindustries.com'))     # Output: False

# Edge case — empty list
empty_list = []
print(binary_search(empty_list, 'dwight@dundermiffin.com'))         # Output: False
```


## 4. Algorithmic Efficiency

- **Time Complexity:** $O(\log N)$ — Halving the problem space at each step dramatically reduces total operations compared to $O(N)$ linear search.
    
- **Space Complexity:** $O(1)$ for iterative implementation.



