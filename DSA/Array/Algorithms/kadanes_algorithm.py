print(float('-inf'))

"""
53. Maximum Subarray

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

def maxSubArray( nums):
    cur_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        cur_sum+= nums[i]
        max_sum = max(cur_sum,max_sum)
        
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

# To return both max_sum and max_sub_arr

def maxSubArray(nums):
    cur_sum = 0
    max_sum = float('-inf')
    start = end = s = 0  # Initialize pointers

    for i in range(len(nums)):
        cur_sum += nums[i]

        # Update max_sum and the corresponding indices
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = s  # Start of the current maximum subarray
            end = i    # End of the current maximum subarray

        # If cur_sum drops below 0, reset it and move the start pointer
        if cur_sum < 0:
            cur_sum = 0
            s = i + 1  # Potential new start of the next subarray

    # Return both the maximum sum and the subarray
    return max_sum, nums[start:end + 1]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubArray( nums)
print(result)  # Output will be (6, [4, -1, 2, 1])
