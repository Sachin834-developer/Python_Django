"""
sort a list without using sort function or sorted function



"""
import logging

my_list=[4,2,1,5,3]
"""
# Bubble sort
for i in range(len(my_list)-1):#0,1,2,3
    for j in range(len(my_list)-1):#0,1,2,3,
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]

for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i]>my_list[j]:
            my_list[i],my_list[j]=my_list[j],my_list[i]

print(my_list)
"""
##############################################################################
"""
Sort a dictionary 

sort dictionary with dict copmrehension

"""
my_dict={5:'a',2:'b',4:'c',1:'d',3:'e'}
print(my_dict)
temp_dict=sorted(my_dict.items())
print(temp_dict)
my_dict2={}

print(temp_dict)
for i in temp_dict:
    print(i)

my_dict2 = {key:value for key,value in sorted(my_dict.items()) }
print(my_dict2)

