"""
1. Print Statement vs. Print Function

print "Hello, World!"  Python 2.x: print is a stateme

print("Hello, World!")  Python 3.x: print is a function, so parentheses are required


2. Integer Division

Python 2.x: Division of two integers results in floor division (i.e., it truncates towards zero)
print 3 / 2  # Output: 1

Python 3.x: Division of two integers results in floating-point division by default
print(3 / 2)  # Output: 1.5

For floor division, you need to use the // operator in both versions:
print(3 // 2)  # Output: 1

3.xrange() vs. range()

Python 2.x: range() returns a list, and xrange() returns an iterator, which is more memory efficient for large ranges.

for i in xrange(1000000):  # Memory efficient
    pass

Python 3.x: range() behaves like xrange() in Python 2, returning an iterator.

for i in range(1000000):  # Memory efficient
    pass

    
4. Functions Returning Iterators

 Python 2.x: Some functions like map(), filter(), and zip() return lists

 Python 3.x: These functions return iterators, which is more memory efficient

 list(map(lambda x: x * 2, [1, 2, 3]))  # Convert iterator to list if needed

 
 5. Dictionary Changes

 Python 2.x: Methods like dict.keys(), dict.values(), and dict.items() return lists.

 Python 3.x: These methods return view objects (iterators) instead of lists, providing better performance in large dictionaries.

 d = {'a': 1, 'b': 2}
print(d.keys())  # dict_keys object


6. Type Annotations

Python 3.x: Introduced type annotations, allowing optional type hints for variables and function arguments. This is useful for 
static type checkers like mypy.

def add(x: int, y: int) -> int:
    return x + y

WHAT is GIL in python ?

Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mutex (mutual exclusion) that protects access to Python objects and prevents multiple native threads from executing Python bytecode at once. This lock is necessary because CPython (the most widely used implementation of Python) is not thread-safe. The GIL ensures that only one thread can execute Python code at a time, even if multiple threads are active in a process.

The GIL makes Python's multithreading suboptimal for CPU-bound tasks. Even if you create multiple threads to utilize multiple CPU cores, the GIL restricts execution to a single core at any time. This limits the performance benefits of multithreading for CPU-bound tasks (e.g., heavy computations) because the threads can't run in true parallelism due to the GIL.















"""
