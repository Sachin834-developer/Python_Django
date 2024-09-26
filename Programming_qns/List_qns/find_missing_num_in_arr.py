
"""
 find the missing number from the list
 """       
"""
to find the sum of the n natural numbers is  = n(n+1) // 2 ; floor div to get non-dec value

ex: for first 5 nums ie., [1,2,3,4,5] = 5*(5+1) // 2 =5*6 // 2 = 30 // 2 = 15 

to find the missing num , find the total sum of the numbers and then find the sum of the given array

then substract both of them to find the missing num
"""
inp_list = [1,2,3,4,6,7,8,9,10]

def find_missing_num(arr,n):
    total_sum_of_arr = n*(n+1) // 2
    return total_sum_of_arr - sum(arr)

print(find_missing_num(inp_list,10))
