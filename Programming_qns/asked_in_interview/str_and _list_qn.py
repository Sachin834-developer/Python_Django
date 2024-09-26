# # print ‘coforge’ from ‘C@###$|\f*23org9900666*^e!1245’

# my_str = "C@###$|\f*23org9900666*^e!1245"
# outpt = ""
# for char in my_str:
#     # print(char)
#     if char.isalpha():
#         outpt += char

# print(outpt)

# [1,2,3,7,23,5,8,13,27] find the third highest element
list_1 = [1, 2, 3, 7, 23, 5, 8, 13, 27]
output = []
prev = list_1[0]
max = 0
for num in list_1:
    if num > max:
        max = num
        old_val = max
        output.append(max)
    elif num > old_val:
        output.append(num)
print(max)
print(output)

"""

# [1,2,3,7,23,5,8,13,27] find the third highest element
list_1 = [15,1, 2, 3, 7, 23, 5, 8, 13, 27,14]

n = len(list_1)
for i in range(n):
    for j in range(n-i-1):
        if list_1[j] > list_1[j+1]:
            list_1[j],list_1[j+1] = list_1[j+1],list_1[j]

print(list_1[-3])

"""


# 04th_july_2024 , Sumanth Norwin Tech
def find_largest_nums(n):
    list1 = [21, 4, 67, 10, 1, 5, 98]
    output = []

    for i in range(len(list1) + 1):
        for j in range(i, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return [list1[-i] for i in range(1, n + 1)]


print(find_largest_nums(3))

# 2nd program
Attendence = {
    "mon": [1, 2, 3, 4, 5],
    "tue": [1, 0, 3, 4, 0],
    "wed": [0, 2, 0, 4, 0],
    "thu": [1, 0, 0, 0, 5],
    "fir": [1, 2, 0, 0, 5],
}

output = {}
for key, value in Attendence:
    count = 0
    for num in value:
        if num != 0:
            count += 1
    output[key] = count
print(output)
