"""
1.*args and ** kwargs

*args

*args allows you to pass a variable number of positional arguments to a function.
Inside the function, *args is treated as a tuple containing all the additional positional arguments
passed.

When to Use: Use *args when you want your function to accept any number of positional arguments
 without having to define them explicitly in the function signature.

"""


def print_values(*args):
    print(args)  # treats as tuple

    for value in args:
        print(value)


print_values(1, 2, 3)
print_values("a", "b", "c", "d")


"""
**kwargs (Variable-Length Keyword Arguments)

Purpose: **kwargs allows you to pass a variable number of keyword arguments to a function. Inside
 the function, **kwargs is treated as a dictionary where the keys are the argument names (as strings) 
 and the values are the corresponding values passed to the function.

When to Use: Use **kwargs when you want your function to accept any number of keyword 
arguments without having to define them explicitly in the function signature.

"""


def print_key_value_pairs(**kwargs):
    print(kwargs)  # treats as dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_key_value_pairs(name="Alice", age=30, city="New York")


"""
2. Lists vs Tuple

Feature 	                            List	                        Tuple
Mutability	                  Mutable (can change)	            Immutable (cannot change)
Syntax	                       Defined using []	                Defined using ()
Performance	                  Slower due to flexibility	        Faster due to immutability
Memory Usage	              Larger due to dynamic sizing	    Smaller due to fixed size
Use Cases	                 When the collection will change	When the collection should remain constant
Hashability	                Not hashable (cannot be used as     Hashable (can be used as keys if all 
                                keys in dictionaries)	                    elements are hashable)
                            
Conclusion:

Use lists when you need a dynamic collection that can grow, shrink, or change over time.
Use tuples when you need a fixed collection of elements, or when you want to ensure data integrity
 by preventing modification. They are also useful when you need a lightweight, memory-efficient
   collection.

   
** Hashability **: 
means that an object can be hashed (has a fixed hash value) and can be 
used as a dictionary key or a set element.

Immutable objects like integers, strings, and tuples are hashable.

Mutable objects like lists and dictionaries are not hashable because their contents can 
change, affecting their hash values.


In Python, hashability refers to the property of an object that allows it to be used as a key in a dictionary or as an element in a set. For an object to be hashable, it must meet two requirements:

Immutability: The object must be immutable, meaning that its state cannot change after it is created. This is because the object's hash value (a unique integer representing the object) must remain constant during its lifetime.

__hash__() and __eq__() Methods: The object must implement a __hash__() method (which returns its hash value) and an __eq__() method (which defines how equality between objects is determined). These methods are used by Python to compare objects when performing operations like dictionary lookups or set membership checks.

Hashable Objects:
Immutable built-in types like int, float, str, and tuple (if all of its elements are hashable) are hashable by default.
Custom classes can also be hashable if they implement __hash__() and __eq__() methods.
Unhashable Objects:
Mutable types like list, dict, and set are not hashable because their contents can change, which would invalidate their hash value. Since their state can change, Python cannot rely on a consistent hash value to perform operations like dictionary key lookups or set membership checks.

Why Hashability Matters:
Dictionaries: In Python, dictionaries use hash values to quickly look up keys. If an object is hashable, it can be used as a key in a dictionary.
Sets: Sets also rely on hash values to efficiently determine membership and uniqueness. Only hashable objects can be added to a set.
Example of Hashable and Unhashable Objects:
Hashable (Immutable) Example:

python
Copy code
my_dict = {(1, 2, 3): "a tuple key", "name": "Alice", 42: "an integer key"}
print(my_dict[(1, 2, 3)])  # Output: a tuple key
In this example, a tuple, a string, and an integer are used as dictionary keys because they are hashable.

Unhashable (Mutable) Example:

python
Copy code
my_list = [1, 2, 3]
# my_dict = {my_list: "a list key"}  # This will raise a TypeError because lists are not hashable
In this example, using a list as a dictionary key will raise a TypeError because lists are mutable and therefore not hashable.

How to Check if an Object is Hashable:
You can check if an object is hashable by using the hash() function. If the object is hashable,
 hash() will return an integer representing its hash value. If the object is not hashable,
Python will raise a TypeError.

print(hash("hello"))  # This will work, as strings are hashable
print(hash((1, 2, 3)))  # This will work, as tuples are hashable
# print(hash([1, 2, 3]))  # This will raise a TypeError, as lists are not hashable

"""

myset = {
    1,
    2,
    3,
    [
        2,
        3,
    ],
}
print(myset)  # TypeError: unhashable type: 'list' we cannot use lists inside set.
# because it is unhashable
print(hash(myset))


"""
3. Exception: Tuples with Mutable Elements
While the tuple itself is immutable, the objects contained within the tuple might be mutable.
 For example, if a tuple contains a list (which is mutable), the list inside the tuple can be
modified, even though the tuple cannot be.


"""
# Ex:1
# A tuple containing a list
my_tuple = (1, 2, [3, 4])

# The tuple itself is immutable, so you can't reassign elements directly
# my_tuple[0] = 10  # This would raise a TypeError

# However, the list inside the tuple is mutable, so you can modify the list
my_tuple[2].append(5)  # Modifying the list inside the tuple
print(my_tuple)  # Output: (1, 2, [3, 4, 5])

# Ex: 2
# Tuple containing a dictionary (mutable object)
my_tuple = (1, {"key": "value"}, 3)

# You cannot change the tuple directly
# my_tuple[0] = 10  # This will raise a TypeError

# But you can modify the dictionary inside the tuple
my_tuple[1]["key"] = "new value"  # Modifying the dictionary inside the tuple
print(my_tuple)  # Output: (1, {'key': 'new value'}, 3)


"""
Summary:

4. " == vs is " operrator 

== checks for equality of values.
is checks for identity (whether two references point to the same object in memory).

"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True (because the lists have the same content)
print(a is b)  # Output: False (because a and b are different objects in memory)


"""
5.           *** MRO (Method Resolution Order)  *** 
            
determines the order in which methods are resolved in a class hierarchy, particularly with multiple inheritance.

Python uses the C3 linearization algorithm to calculate the MRO, ensuring that child classes 
are checked before their parent classes and that the order of inheritance is respected.

You can view the MRO using the .__mro__ attribute or the mro() method.
MRO is essential for handling multiple inheritance, avoiding ambiguity, and ensuring consistent 
method resolution.


"""


class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")


class C(A):
    def method(self):
        print("Method in C")


class D(B, C):
    pass


d = D()
d.method()

print(D.mro())
"""
OUTPUT

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

"""


##########################################################################################

# PYTHON PRINT()  FUNCTION
# Basic Syntax: print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# Format Strings: Use +, str.format(), f-strings, or % for formatting output.

print("sachin", sep=",", end=" ", flush=False)


print("without", end="")
print("newline!")  # Output: HelloWorld!

# Printing Without a Newline
"""
Printing to a File:
You can redirect the output to a file using the file parameter:
"""
with open("output.txt", "r") as f:
    print("Hello World", file=f)
