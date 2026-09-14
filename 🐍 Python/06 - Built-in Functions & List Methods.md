

## 06. Bucket List Project (`bucket_list.py`)

Combining concepts of list creation and iteration to output a bucket list.


### 📝 Bucket List Exercise (`bucket_list.py`)

```python
# bucket_list.py

things_to_do = [
  'Create the dopest learn to code platform ever.',
  'Hike the Pacific Crest Trail.',
  'Build an A-frame house and raise some goats.',
  'Live somewhere in Asia for a year.',
  'Release an album.',
  'Write a book.',
  'Reach 100k subscribers on YouTube.',
  'Road trip with the fam.',
  'Open a cozy diner upstate.',
  'Grow old with no regrets.'
]

for thing in things_to_do:
  print(thing)
```



## 07. Nested Lists & Matrices

A **nested list** is a list that contains other lists as elements.

```python
# Mixed nested list
my_list = ['a', 'b', 'c', [1, 2, 3]]

# Accessing elements inside a nested list
print(my_list[3][1]) # Output: 2
```



### 🔹 Matrices (2D Lists)

When every item in a list is a nested list of equal length, it forms a **matrix** or **2D list** (organized in rows and columns).


```python
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
```


#### Tic-Tac-Toe Board Example


```python
board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]

# Accessing row 2, column 1
row = 2
column = 1
print(board[row][column]) # Output: x
```
