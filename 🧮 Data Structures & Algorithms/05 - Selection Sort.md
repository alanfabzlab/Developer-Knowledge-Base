
# 05. Selection Sort & Quadratic Efficiency


## 1. How Selection Sort Works

**Selection Sort** is an in-place comparison sorting algorithm. It divides the input list into two parts:
1. A **sorted sublist** built up from left to right at the front of the list.
2. An **unsorted sublist** occupying the remainder of the list.

In each iteration (or pass), the algorithm finds the smallest element in the unsorted sublist and swaps it with the leftmost unsorted element.


---


## 2. Python Implementation

The implementation relies on **nested loops**:
- **Outer loop (`j`):** Tracks the dividing marker between the sorted and unsorted sections.
- **Inner loop (`i`):** Scans the unsorted section to find the minimum element's index.


Python

```python
def swap(input_list, index_1, index_2):
    temp = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = temp
    return input_list

def selection_sort(my_list):
    # Outer loop moves boundary of unsorted subarray
    for j in range(len(my_list)):
        lowest_index = j
        
        # Inner loop finds the smallest element in unsorted portion
        for i in range(j + 1, len(my_list)):
            if my_list[i] < my_list[lowest_index]:
                lowest_index = i
                
        # Swap found minimum element with first unsorted element
        my_list = swap(my_list, j, lowest_index)
        
    return my_list

# Example usage
numbers = [8, 15, 4, 2]
print(f"Sorted list: {selection_sort(numbers)}")  # Output: [2, 4, 8, 15]
````


## 3. Quadratic Efficiency Analysis ($O(N^2)$)

### Comparison Count

For a list of size $n$:

- **Pass 1:** Performs $n - 1$ comparisons.
    
- **Pass 2:** Performs $n - 2$ comparisons.
    
- **Pass 3:** Performs $n - 3$ comparisons.
    

Total comparisons:

$$(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$$

git add . && git commit -m "feat(dsa): add 05 - Selection Sort note and update README" && git push origin main
### Big-O Classification

Approximating worst-case operations as list size grows:

- Both **Selection Sort**, **Bubble Sort**, and **Insertion Sort** make roughly $n \times n = n^2$ comparisons.
    
- **Time Complexity:** $O(N^2)$ (Quadratic Time).
    
- **Space Complexity:** $O(1)$ (Auxiliary Space — sorted in-place).
    

> **Takeaway:** Quadratic algorithms slow down dramatically as input size grows. For large datasets, algorithms like **Merge Sort** ($O(N \log N)$) are significantly faster.
