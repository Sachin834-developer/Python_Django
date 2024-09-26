

# Move Zeros  to the end of the list
list=[1,0,2,1,0,4,5]
list1=[1,0,2,1,0,4,5]

n=len(list)
# for i in range(n):
#     for j in range(i+1,n):
#         if list[i]==0:
#             list[i],list[j]=list[j],list[i]
# print(list)

for i in range(n):
    # for j in range(i+1,n):
    if list[i]==0:
        list[i],list[i+1]=list[i+1],list[i]
print(list)

# Move Zeros  to the start of the list
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[j]==0:
            list1[j],list1[i]=list1[i],list1[j]
print(list1)

# chatgpt

my_list = [1, 0, 2, 1, 0, 4, 5]
zero_list = [num for num in my_list if num == 0]
non_zero_list = [num for num in my_list if num != 0]

result_list = non_zero_list + zero_list

print(result_list)

