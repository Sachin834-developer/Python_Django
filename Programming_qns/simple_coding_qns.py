# 1. LIST extend vs Append method
list1 = list(range(0,10))

list2 = list(range(11,16))

list1.extend(list2)  # extend method loop thrpugh the inp data and adds each element to the existing list.
list2.append(list1)  # appends the whole list as a element in to the list2 

print(list1)
print(list2)
print(list2[5])  # added as a single element 



# 2. diff b/w is and == operator 

# '==' checks if the values of two objects are the same (equality)
# 'is' checks if two objects are the same object in memory (identity).
# is should be used when you need to check if two references point to the same object,
#  while == should be used to compare the values of two objects.
# FOR MUTTABLE datatypes like int, string and tuples python points to same reference address  for example
#  FOR string 
a ='ssv'
b= 'ssv'
print(a is b) 
print(a == b)

#  FOR Tuple 
t1 =(1,2,3,4,5)
t2 =(1,2,3,4,5)
print(t1 is t2)
print(id(t1) == id(t2))

# #  FOR Integer
i1 = 12233444
i2 = 12233444
print(id(i1) == id(i2))
print(i1 is i2)
print(i1 == i2)

# IMMPUTABLE Example
l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1 is l2)
print(id(l1) == id(l2))