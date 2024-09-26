"""
Searching Algorithms:
    1. Linear search  : Time O(n)
    2. Binary Search   : Time : O(log n)   n is size of the array   

    binary search works on only sorted arrays

    .Binary search can be implemented by 2 approachs
            1. Iterative approach
            2. Recursive approach

     Recursions functions donot have for loops
"""
nums = [1,2,3,4,5,6,7,8,9]
target = 1
def binary_search(nums:list,target):
    left = 0
    right  = len(nums) - 1
    mid = left + right // 2

    while left <= right:
        print(f'{left=},{right=}')
        mid = (left + right )// 2 # if your array len is even  then add + 1 , 
        print(f'{mid=}')
        if nums[mid]  ==  target:
            return mid
        
        if target < nums[mid]:
            right  = mid - 1
        else:
            left = mid + 1
    return -1
        
print(binary_search(nums=nums,target=target))

