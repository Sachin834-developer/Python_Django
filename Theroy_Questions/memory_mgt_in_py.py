"""
How does Python manage memory?

Python manages memory using an automatic memory management system that includes:

Memory Allocation: Python uses private heap space to store objects and data structures. The Python 
memory manager handles this heap space, and the programmer does not have direct access to it. 
The memory manager ensures efficient memory allocation and deallocation.
Object Lifecycle: When an object is created, memory is allocated, and when the object is no longer 
needed, memory is deallocated.

*** Reference Counting ***

Python uses reference counting as the primary mechanism to manage memory. Every object in Python 
maintains a count of references, which indicates how many times the object is being referenced in 
the code.

When a new reference to an object is created, its reference count is incremented, and when a reference 
is deleted (e.g., the variable pointing to it goes out of scope), the reference count is decremented.

When the reference count of an object drops to zero, the memory occupied by that object is
 automatically deallocated.


*** Garbage Collection ***

While reference counting is effective for most cases, it cannot handle circular references 
e.g., two or more objects referencing each other).
Python has a built-in garbage collector that detects circular references and reclaims memory. 
The garbage collector periodically checks for objects that are no longer accessible from any part 
of the code, even if their reference count is not zero (due to circular references).

The garbage collector uses generational garbage collection to manage memory. Objects are divided 
into generations (young, middle-aged, old), and the garbage collector works more frequently on younger 
objects since they are more likely to be short-lived.


In summary, Python uses a combination of reference counting, garbage collection, memory pools, 
and arenas to manage memory efficiently. The built-in memory manager handles most tasks automatically,
allowing developers to focus on coding without worrying much about memory allocation and deallocation. 
However, understanding how memory is managed can help optimize performance, especially in 
memory-intensive applications.

"""

x = [1, 2, 3]  # reference count for list object increases
y = x          # reference count for list object increases
del x          # reference count decreases
del y          # reference count drops to 0, memory is deallocated
