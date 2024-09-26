"""
find the max and min value in a list without using builtin min and max functions.


"""

my_list=[10,20,30,40,50,60]

min_num=my_list[0]
max_num=my_list[0]

for i in range(len(my_list)-1):
    # for j in range(i+1,len(my_list)-1):
        if my_list[i]>max_num:
            max_num = my_list[i]
        # else:
        #     max_num=my_list[j]

        if my_list[i]<min_num:
            min_num=my_list[i]
        # else:
        #     min_num=my_list[j]

print(min_num,'is a minimum number')
print(max_num,'is a maximum number')

