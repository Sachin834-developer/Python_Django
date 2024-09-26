my_dict = {'name': 'Alice', 'age': 30}
"""
1.dict.get(key, default)
Returns the value for the specified key if it exists; otherwise, it returns the default value.
"""
# print(my_dict['location'])  #KeyError: 'location'
print(my_dict.get('location','invalid key')) #invalid key

print(my_dict.keys()) #Returns a view object that displays  a list of all the keys in the dictionary.
print(my_dict.values()) #Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.items()) #Returns a view object that displays a list of dictionary's key-value tuple pairs.


# 2 ways of inserting the new key value pairs to the dictionary.
my_dict['salary'] = 30000

"""
dict.update([other]): updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
"""
new_dict={'mob_no':82727,'blod_grp':'O+ve'}
my_dict.update({'lang':'python'})  # updating new key val pairs to dict.
my_dict.update(new_dict)    # inserting or updating a new dict to existing dict

print(my_dict.items())

"""
 dict.pop(key, default) :Removes the specified key and returns the corresponding value. 
 If the key is not found, default is returned.

 dict.popitem() : Removes and returns the last inserted key-value pair as a tuple.

"""
print(my_dict.pop('age1','invalidkey1'))
print(my_dict.popitem())
print(my_dict.items())

"""
dict.setdefault(key, default) : Returns the value of the specified key if it exists. If not, 
inserts the key with the default value.

"""

print(my_dict.setdefault('pincode','577513')) # As key pincode is not presents it will inserts with the default specified value
print(my_dict.items())


