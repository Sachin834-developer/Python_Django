"""
1. Variable length slinding window
2. Fixed length sw


1. Variable length slinding window

Window is anything between l and r 

In sliding window we always to need to check is our window valid

validation condition differs from problem to problem

 1. as long as our substring is valid we keep on moving R 

 To find window length that is always window len  w = (r-l) + 1 

 2. once our substr fails the validation , then we will move our l and check the validation again
     then if valid move R otherwise L 

 3. when R gets to the end thats when we complete the group.

"""
# Ex. Find the longest substring without repeating the charchaters
s="abcabcbb" 
# output 3 with 'abc'


def findLongestSubstring(s:str):
    l = 0
    sett = set()
    longest = 0
    for r in range(len(s)):  #O(n) as looping 
        while s[r] in sett: 
            sett.remove(s[l])  # O(1)
            l+=1

        w= (r-l) + 1
        longest = max(w,longest)
        sett.add(s[r])

    return longest
print(findLongestSubstring(s))

"""
2. Fixed length sliding window

in fixed length  in qn we will get some const vakue of length of the window 

Ex:

643. Maximum Average Subarray I
Easy
Topics
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:
"""
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = 0
        # max_avg = 0
        n = len(nums)
        if k==n:
            return sum(nums)/k

        for i in range(k):
            cur_sum  += nums[i]

        max_avg = cur_sum/k

        for j in range(k,n):
            cur_sum += nums[j]
            cur_sum -= nums[j-k]

            avg = cur_sum/k
            max_avg = max(avg,max_avg)

        return max_avg
