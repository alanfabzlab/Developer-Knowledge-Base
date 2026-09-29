
# 05. Selection Sort & Quadratic Efficiency


**Spanish version:** [05 - Ordenamiento por Selección.md](05%20-%20Ordenamiento%20por%20Selecci%C3%B3n.md)

**Course:** Data Structures & Algorithms
**Topic:** Nested Loops, In-Place Sorting, Element Swapping & Quadratic Efficiency
**Tags:** `#dsa` `#sorting` `#selection-sort` `#complexity`



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

# Boss HP values in the order the bestiary scans them
boss_health = [480, 120, 950, 300]  # ember_knight, frost_wraith, stone_golem, void_reaper

print(f"Sorted HP: {selection_sort(boss_health)}")      # Output: Sorted HP: [120, 300, 480, 950]
print(f"Same list, sorted in place: {boss_health}")     # Output: Same list, sorted in place: [120, 300, 480, 950]
```


### Watching the Sorted Section Grow

Printing the list after every pass makes the two sections visible: the first `j + 1` positions are final, everything after them is still up for grabs.

Python

```python
def selection_sort_trace(my_list):
    for j in range(len(my_list)):
        lowest_index = j

        for i in range(j + 1, len(my_list)):
            if my_list[i] < my_list[lowest_index]:
                lowest_index = i

        my_list = swap(my_list, j, lowest_index)
        print(f"Pass {j + 1}: {my_list}")

    return my_list

selection_sort_trace([480, 120, 950, 300])
```

```text
Pass 1: [120, 480, 950, 300]
Pass 2: [120, 300, 950, 480]
Pass 3: [120, 300, 480, 950]
Pass 4: [120, 300, 480, 950]
```

- **Pass 1** locks in `120` and swaps it with the current first element.
    
- **Pass 2** locks in `300`, swapping it with `480` rather than shifting everything one slot to the right.
    
- **Pass 3** locks in `480`, leaving `950` in the only position left.
    
- **Pass 4** has an empty inner loop, so the final pass changes nothing.


## 3. Quadratic Efficiency Analysis ($O(N^2)$)

### Comparison Count

For a list of size $n$:

- **Pass 1:** Performs $n - 1$ comparisons.
    
- **Pass 2:** Performs $n - 2$ comparisons.
    
- **Pass 3:** Performs $n - 3$ comparisons.
    


Total comparisons:

$$(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$$

An instrumented run confirms the formula, and shows that the count is fixed in advance of the data:

Python

```python
def selection_sort_comparisons(my_list):
    comparisons = 0

    for j in range(len(my_list)):
        lowest_index = j

        for i in range(j + 1, len(my_list)):
            comparisons += 1
            if my_list[i] < my_list[lowest_index]:
                lowest_index = i

        my_list = swap(my_list, j, lowest_index)

    return comparisons

for size in (4, 8, 16, 1000):
    print(size, selection_sort_comparisons(list(range(size))))
```

```text
4 6
8 28
16 120
1000 499500
```

A bestiary of 1000 bosses costs **499,500 comparisons** — half a million operations to put the scan order in sequence, and the same count applies even when the list arrives already sorted. The number of comparisons depends only on $n$, never on the input.

### Big-O Classification

Approximating worst-case operations as list size grows:

- Both **Selection Sort**, **Bubble Sort**, and **Insertion Sort** make roughly $n \times n = n^2$ comparisons.
    
- **Time Complexity:** $O(N^2)$ (Quadratic Time).
    
- **Space Complexity:** $O(1)$ (Auxiliary Space — sorted in-place).
    
> **Takeaway:** Quadratic algorithms slow down dramatically as input size grows. For large datasets, algorithms like **Merge Sort** ($O(N \log N)$) are significantly faster. Selection Sort's one advantage is that it performs at most $n - 1$ swaps, which matters when writing to memory is expensive — but the comparisons still dominate, so it is a teaching algorithm rather than a production one.


---

## 4. Efficiency Demo & Comparative Analysis

The formula above predicts the count, so it is worth confirming it — and checking how the three quadratic sorts compare against each other on identical data.

Python

```python
# Each variant only counts comparisons; the sort still reorders the list
def selection_sort_counted(my_list):
    comparisons = 0
    for j in range(len(my_list)):
        lowest_index = j

        for i in range(j + 1, len(my_list)):
            comparisons += 1
            if my_list[i] < my_list[lowest_index]:
                lowest_index = i

        my_list = swap(my_list, j, lowest_index)

    return comparisons

def bubble_sort_counted(my_list):
    comparisons = 0

    for j in range(len(my_list) - 1):
        for i in range(0, len(my_list) - 1 - j):
            comparisons += 1
            if my_list[i] > my_list[i + 1]:
                my_list = swap(my_list, i, i + 1)

    return comparisons

def insertion_sort_counted(my_list):
    comparisons = 0

    for i in range(1, len(my_list)):
        key = my_list[i]
        k = i - 1

        while k >= 0:
            comparisons += 1
            if my_list[k] <= key:
                break
            my_list[k + 1] = my_list[k]
            k -= 1

        my_list[k + 1] = key

    return comparisons
```

Running all three over the same 10-element list, first already ordered and then reversed:

```python
ordered = [20, 30, 45, 55, 60, 70, 80, 85, 90, 95]
reversed_scan = ordered[::-1]

print('n = 10, already ordered')
print('Selection:', selection_sort_counted(ordered[:]))
print('Bubble:   ', bubble_sort_counted(ordered[:]))
print('Insertion:', insertion_sort_counted(ordered[:]))

print('\nn = 10, reverse ordered')
print('Selection:', selection_sort_counted(reversed_scan[:]))
print('Bubble:   ', bubble_sort_counted(reversed_scan[:]))
print('Insertion:', insertion_sort_counted(reversed_scan[:]))
```

```text
n = 10, already ordered
Selection: 45
Bubble:    45
Insertion: 9

n = 10, reverse ordered
Selection: 45
Bubble:    45
Insertion: 45
```


### Key Takeaways from the Demo

- **Exact Comparison Formula:** For $n = 10$, Selection Sort performs exactly $(10 \times 9) / 2 = 45$ comparisons, and the count is identical in both runs. Only $n$ decides the total, never the input order.
    
- **Bubble Sort vs. Insertion Sort:** Bubble Sort also reports 45 both times, because the naive version always runs all $n - 1$ passes. Insertion Sort drops to 9 on the ordered list — exactly the $n - 1$ case — and climbs to 45 when the data is reversed.
    
- **The Real Distinction:** All three share the $O(N^2)$ worst case, but only Insertion Sort improves on already-sorted input, which is why it is the one worth reaching for when partial order is likely.


---

## 5. Chapter Review & Algorithmic Patterns

This chapter completes the core comparison of search and sorting fundamentals:

- **Linear Search:** Scans every item sequentially and works on an unsorted list ($O(N)$).
    
- **Binary Search:** Repeatedly divides a sorted list in half ($O(\log N)$), paying for a sort up front.
    
- **Selection Sort:** Uses **nested `for` loops** to grow a sorted section and place the minimum element of the unsorted remainder on every pass, for quadratic work ($O(N^2)$).

The pattern running through all three is the same trade: the more structure the algorithm is allowed to assume about the input, the less work it has to do. Linear Search assumes nothing and pays $O(N)$. Binary Search assumes sortedness and pays $O(\log N)$. Selection Sort makes no assumptions and pays $O(N^2)$.

