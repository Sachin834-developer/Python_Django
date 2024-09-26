keys = ['a','b','c','d','e']
values = [1,2,3,4,5]


mydict={key:value for key ,value in zip(keys,values)}

print(mydict)



list1=[1,2]
dic=dict.fromkeys(range(5), list1)
 
print(dic)

# Creating a nested dictionary of squares for numbers 0 to 2
nested_dict = {x: {y: y*y for y in range(3)} for x in range(3)}
print(nested_dict)
# Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}


#############
# Exmaple 3

# Existing dictionary
original_dict = {'apple': 5, 'banana': 12, 'cherry': 2, 'date': 10}

# Dictionary comprehension to filter items with value > 5
filtered_dict = {key: value for key, value in original_dict.items() if value > 5}

print(filtered_dict)
# Output: {'banana': 12, 'date': 10}

# Example 4
# List of items
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
from collections import Counter
print(Counter(items))
frequency  = { item: items.count(item) for item in items}
print(frequency)
# Output: {'cherry': 1, 'banana': 3, 'apple': 2}




