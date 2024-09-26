#Verifying Memory Address of Immutable Objects (e.g., Integers)
x = 10
y = 10

print("Memory address of x:", id(x))
print("Memory address of y:", id(y))
print("x and y have the same memory address:", id(x) == id(y))
"""
In this case, since integers are immutable and small integers are cached in Python, x and y may 
share the same memory address, and id(x) will equal id(y)

"""

# Verifying Memory Address of Mutable Objects (e.g., Lists)


list1 = [1, 2, 3]
list2 = list1  # list2 is a reference to the same list object as list1
list2.append(4)
# print(list1)

print("Memory address of list1:", id(list1))
print("Memory address of list2:", id(list2))
print("list1 and list2 have the same memory address:", id(list1) == id(list2))

tuple1= (1,2,3)
tuple2 = tuple1


print("Memory address of list1:", id(tuple1))
print("Memory address of list2:", id(tuple2))
print("list1 and list2 have the same memory address:", id(tuple1) == id(tuple2))


# Shallow copy vs Deep Copy

import copy

orginal_list = [1,2,3,4,5]

normal_copy = orginal_list
shallow_copy = copy.copy(orginal_list)
deep_copy = copy.deepcopy(orginal_list)


print("normal copy",id(orginal_list) == id(normal_copy))  
print("shallow copy",id(orginal_list) == id(shallow_copy))
print("Deepy copy", id(orginal_list) == id(deep_copy))
"""

Normal Copy : in normal won't create the new memory new address it will share the same memory address

Shallow_copy :  will have a different memory address from original_list because it creates a new top-level 
 object, but the inner objects (if any) would share memory addresses with the original.
 Note : creates new memory for only top-level objects not for nested objects in a list

Deep_copy : will have a completely independent memory address, including its nested objects,
 because deepcopy recursively copies all objects.

 Shallow copies may share inner objects (same memory addresses for nested objects), whereas deep copies
create entirely new objects with different memory addresses.
"""

# Example

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

# Memory address of outer lists
print("Memory address of original_list:", id(original_list))
print("Memory address of shallow_copy:", id(shallow_copy))
print("Memory address of deep_copy:", id(deep_copy))

# here the shallow copy also creates the new memory address for the copied object.
print("original_list and shallow_copy share the same memory address:", id(original_list) == id(shallow_copy))
print("original_list and deep_copy share the same memory address:", id(original_list) == id(deep_copy))

# Here the nested objects of the shallow copy shares same memory address 
print("original_list[0] and shallow_copy[0] share the same memory address:", id(original_list[0]) == id(shallow_copy[0]))
print("original_list[0] and deep_copy[0] share the same memory address:", id(original_list[0]) == id(deep_copy[0]))
