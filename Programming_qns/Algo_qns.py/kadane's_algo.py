
lst=[1, 2, 3, -2, 5]
# lst=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

# o/p 9
def max_sum_subarr(lst):
    max_sum=lst[0]
    cur_sum=lst[0]
    for i in range(1,len(lst)):
        cur_sum=max(lst[i] , cur_sum+lst[i])
        max_sum=max(max_sum,cur_sum)
    return max_sum

print(max_sum_subarr(lst))