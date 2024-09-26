list = [1, 2, 2, 3, 3, 4, 3, 2, 2, 5, 6, 6, 7, 8]
"""
my_list=[]
[my_list.append(num)  for num in list if num not in my_list]  
print(my_list)
"""
# Example if else in the list comprehension
# [my_list.append(num) if num not in my_list else my_list.append(10) for num in list  ]
"""
my_dict={}
for num in list:
    if num in my_dict.keys():
        my_dict[num]+=1
    else:
        my_dict[num]=1

print(my_dict)

output=[]
for key,value in my_dict.items():
    if my_dict[key] <= 1:
        output.append(key)
print(output)


# using set 
new_list=set(list)
print(new_list)

"""

input_str = "aaaaabbbbcccdd"
# 5a4b3c2d
output = ""
char = input_str[0]
count = 0
for ch in input_str:
    if ch == char:
        count += 1
    else:
        output += str(count) + char
        char = ch
        count = 1
print(dir())
output += str(count) + char
print(output)


