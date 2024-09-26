"""
Lambda Functions:

lambda fucntions are define with the the use of lambda keyword for one time usage of a block of code , its syntax goes like
Good for performing short operations/data manipulations.
 Syntax: lambda varibales: expression

 there won't use explict return keyword in lambda functions

ex:
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())

Use can be demonstrated by map , filter and reduce

Map:
used to apply the sequence of elements to a certain condition and get the result 


Filter:
when function returns True or False actually filters the data which are True and returns only that data
"""
list1=[1,2,3,4,5]

f1=lambda x:x*x
print(f1)
# for i in list1:
#     print(f1(i,i))


# # for map 
list2=map(lambda x:x*x ,list1)
# print(list(list2))

# for filter 
list3=filter(lambda x:x%2==0,list1)
print(list(list3))

#for Reduce
# Python code to illustrate
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

# Here the results of the previous two elements are added to the next element and 
# this goes on till the end of the list like (((((5+8)+10)+20)+50)+100).