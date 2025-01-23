"""
### What is Big O Notation?

Big O notation is a mathematical concept used in computer science to describe the **performance** or **complexity** of an algorithm. Specifically, it provides an upper bound on the time or space (memory) required by an algorithm as a function of the size of its input, usually denoted as \( n \).

### Why is Big O Notation Important?
Big O notation helps in evaluating how an algorithm scales as the input size grows. It focuses on the **worst-case scenario** to ensure that the algorithm performs efficiently even with large inputs.

### Key Concepts
1. **Time Complexity**: Refers to the time it takes for an algorithm to run as a function of the input size \( n \).
2. **Space Complexity**: Refers to the amount of memory an algorithm uses as a function of the input size \( n \).

### Big O Notation Classifications
Here are some of the most common types of time complexities you'll see in algorithms, from fastest to slowest:

#### 1. **O(1) – Constant Time**
- The algorithm's runtime does not depend on the input size \( n \).
- Example: Accessing an element from an array by its index.
```python
def get_first_element(arr):
    return arr[0]  # Always O(1), no matter how large the array is
```

#### 2. **O(log n) – Logarithmic Time**
- The algorithm's runtime increases logarithmically as the input size \( n \) grows. This usually happens in algorithms that repeatedly divide the problem in half.
- Example: Binary search.
```python
def binary_search(arr, target):
    # O(log n) time complexity
```

#### 3. **O(n) – Linear Time**
- The algorithm's runtime grows proportionally to the input size \( n \).
- Example: Traversing an array or list.
```python
def print_all_elements(arr):
    for item in arr:
        print(item)  # O(n), since you go through all elements
```

#### 4. **O(n log n) – Linearithmic Time**
- Often seen in efficient sorting algorithms like merge sort and quicksort.
- Example: Merge Sort, Quick Sort (average case).
```python
def merge_sort(arr):
    # O(n log n) time complexity
```

#### 5. **O(n^2) – Quadratic Time**
- The algorithm’s runtime grows quadratically as the input size increases. Usually happens with algorithms involving nested loops.
- Example: Bubble sort, insertion sort.
```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            # O(n^2), because of the nested loops
```

#### 6. **O(2^n) – Exponential Time**
- The algorithm’s runtime doubles with each additional input element. Typically seen in recursive algorithms that solve smaller sub problems multiple times.
- Example: Solving the Fibonacci sequence with simple recursion.
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # O(2^n)
```

#### 7. **O(n!) – Factorial Time**
- The runtime grows very quickly and is usually impractical for large \( n \). Seen in problems involving permutations, like the traveling salesman problem.
- Example: Generating all permutations of a string.
```python
def generate_permutations(s):
    # O(n!) time complexity
```


### Graphical Representation
Here’s a rough idea of how different time complexities grow as \( n \) increases:

- **O(1)**: Constant, flat line (best scenario).
- **O(log n)**: Slowly increasing curve.
- **O(n)**: Linear, straight line.
- **O(n log n)**: Faster-growing than linear, but slower than quadratic.
- **O(n^2)**: Steeper quadratic curve.
- **O(2^n)**: Exponential growth, shoots up rapidly.
- **O(n!)**: Even steeper than exponential.

### Dropping Constants and Lower-Order Terms
In Big O notation, we **ignore constants and lower-order terms** because they become insignificant as \( n \) grows large.

linear time = a*n+ b


RUles to while calc Big O:

1. Keep the fastest growing term . so  t = a*n
2. Drop constants , t = n  so its O(n)
ex:
t = n O(n)
t=a O(1)
t= a* n**2    t =  n**2   O(n**2)

Ex 2:
  t =  a* n**2 + b* n + c
  Rule no 1 , keep the fastest growing so t =  a* n**2
  O(n**2)
    Reason being
     5 * n**2 + 3 * n + 20   
     for n = 1000
     5000000 + 3000 + 20  here 5000000 is way more bigger than the 3000 so it makes sense to keep only fastest growing term ,

Binary Search : Algorithm's Big O is log n - logrithmic time

if find the searching element in a first itertion itself then iteration 1 = n/2

 for k iterations 
    iteration k  =  n/2**k
     1 =  n/2 ** k
     n = 2**k implement log on both side 
     log2 n  =  log2 **2k
     log2 n =  k * log2 2 then log2 2 =1 , so
     k = log2 n  Big O is 
     K = log n -->
     O(log n)  

For example:
- \( O(3n + 10) \) simplifies to \( O(n) \).
- \( O(5n^2 + 7n) \) simplifies to \( O(n^2) \).

### Summary
- **Big O notation** helps in understanding the efficiency of algorithms.
- It describes how an algorithm's runtime or space grows as the input size increases.
- Focuses on the **worst-case scenario**.
- Common complexities range from **O(1)** (constant time) to **O(n!)** (factorial time).

"""
