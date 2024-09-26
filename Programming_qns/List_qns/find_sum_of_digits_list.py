
input=[2,45,63,53,234]
# output=[2,9,9,8,9]

 # with  Nested Loop
# new_list=[]
# for num in input:
#     num=str(num)
#     sum=0
#     for digit in num:
#         sum+=int(digit)
#     new_list.append(sum)

# print(new_list)

# without Nested Loop
output=[]
for num in input:
    num=str(num)
    output.append(sum(map(int,list(num))))
print(output)

st='sachin'
print(st)
print(list(st))

#chatgpt way

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

input_list = [2, 45, 63, 53, 234]
output_list = [sum_of_digits(num) for num in input_list]

print(output_list)
