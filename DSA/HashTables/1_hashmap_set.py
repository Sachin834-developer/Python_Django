"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
# Time: O(n+m) here n = jewels and m  = stones

# Ex:1
# time complexity of checking op in sets is O(1) and looping in lists is O(n) 
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count=0
        for char in stones:
            if char in s:  # if char in jewels big O is O(m) so totally O(n*m)  to avoid,use set  O(n+m)
                count+=1
        return count


# EX:2
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
"""

# Time : O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s= set()
        for num in nums: # O(n)  for list iteration
            if num in s:  # O(1) const time search op..
                return True
            s.add(num)  # O(1)  cont time
        return False
    
# Ex:3
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

"""

# Time = O(m+n) , Space = O(1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}

        for char in magazine:  # O(n)
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in ransomNote: # O(m)
            if char not in counter:
                return False
            elif counter[char] == 1:
                del counter[char]
            else:
                counter[char] -= 1
        return True