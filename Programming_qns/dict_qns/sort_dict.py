# mydict={200:'apple',100:'bal',400:'cat',300:'dog'}
mydict = {'banana': 3, 'apple': 4, 'cherry': 2, 'date': 5}

#1.
d=sorted(mydict.keys())
# print(d)
mydict2= { i:mydict[i] for i in d }
# print(mydict2)

#2.Sort by Keys
print(dict(sorted(mydict.items(),key=lambda item: item[0]))) # reverse=True to sort in descending order , 

#2. Sort by Values
print(dict(sorted(mydict.items(),key=lambda item:item[1])))

#2.sorted_by_keys_then_values
sorted_by_values_then_keys  = dict(sorted(mydict.items(),key= lambda item : (item[0],item[1])))
print(sorted_by_values_then_keys)

#2.sorted_by_values_then_keys
sorted_by_values_then_keys  = dict(sorted(mydict.items(),key= lambda item : (item[1],item[0])))
print(sorted_by_values_then_keys)


#3.
from collections import OrderedDict
sorted_dict = OrderedDict((k, mydict[k]) for k in sorted(mydict))
print(sorted_dict)


#4. List of dictionaries

product_list = [
    {'name': 'product1', 'quantity': 10},
    {'name': 'product2', 'quantity': 5},
    {'name': 'product3', 'quantity': 15}
]
# print(list(sorted(map(lambda x: x['quantity'],product_list,))))  # roughly
# Sorting by the 'quantity' key
sorted_by_quantity = sorted(product_list, key=lambda x: x['quantity'])

print(sorted_by_quantity)
# Output: [{'name': 'product2', 'quantity': 5}, {'name': 'product1', 'quantity': 10}, {'name': 'product3', 'quantity': 15}]
