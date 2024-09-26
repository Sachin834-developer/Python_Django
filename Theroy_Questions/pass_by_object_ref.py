"""

Everything in Python is an Object: Variables are references (pointers) to objects. When you 
pass a variable to a function, you're passing the reference to the object that the variable 
points to, not the actual object itself.

Immutables:

When you pass an immutable object (e.g., an integer or string) to a function, any changes you make
 within the function will not affect the original object. This is because, when you attempt to modify
   an immutable object, Python creates a new object rather than modifying the original.
"""

def modify(x):
    x = 10  # This rebinds x to a new object, not affecting the original variable

a = 5
modify(a)
print(a)  # Output: 5 (original value unchanged)

"""
Mutuables:

When you pass a mutable object (e.g., a list or dictionary) to a function, the function receives 
a reference to the original object. Any changes made to the object within the function will affect 
the original object.
"""
def modify(lst):
    lst.append(4)  # Modifies the original list

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # Output: [1, 2, 3, 4] (original list modified)

"""
Summary:

Python's argument passing is best described as pass-by-object-reference.
For immutable objects, it behaves similarly to pass-by-value, since modifications result in new objects.
For mutable objects, it behaves similarly to pass-by-reference, since modifications affect the original 
object.

"""