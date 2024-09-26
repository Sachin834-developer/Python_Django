my_dict={}

my_dict['sachin']='tcs'
my_dict2={'guru':'tcs'}


my_dict.update(my_dict2)  # to extend a dict
my_dict.update({'veeru':'inm'})

print(my_dict.setdefault('akash','tcs'))  # returns the value if key is already present else inserts the key with default value and returns the value.
# for key in my_dict:
#     print(key)

print(my_dict[1])
print(my_dict,end="\n",sep='#')
print('string ',' to check print ',' parameters',sep='i')

"""

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
copy_dict=my_dict.copy()
copy_dict_by_var=my_dict

#my_dict.popitem()   # removes the last value and returns  it 
my_dict.pop('veeru') # remove and returns the specified value

# del my_dict
print(copy_dict)
print(my_dict)
print(copy_dict_by_var)
#list1=[1,2,3,4]
#list2=['a','b','c','d']
#print(my_dict.fromkeys(list1,'a',))

try:
    print(my_
    =dict['sachin']) # if key was not present it will throw KeyError
except KeyError:
    print('Key Error')
else:
    print('retrieval successful')
finally:
    print('Exception handling with dicts')
"""