"""
242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""


# Time : n log n
# Space : O(n+m)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        st = sorted(t)

        if ss == st:
            return True
        return False


# Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in s_d:
                s_d[char] = 1
            else:
                s_d[char] += 1
        for char in t:
            if char not in t_d:
                t_d[char] = 1
            else:
                t_d[char] += 1
        return s_d == t_d


"""
Let's break down the time and space complexity for the `isAnagram` function you've provided.

### Time Complexity
1. **Length Check**: `if len(s) != len(t)`: This operation is \(O(1)\) since it's a simple comparison of the lengths of `s` and `t`.
2. **First Loop (`for char in s`)**:
   - This loop iterates through all the characters in `s`.
   - For each character, the dictionary `s_d` is accessed and updated, which is an \(O(1)\) operation on average.
   - Therefore, this loop runs in \(O(n)\) time, where \(n\) is the length of `s` (and `t`).
3. **Second Loop (`for char in t`)**:
   - Similarly, this loop iterates through all the characters in `t`, and dictionary `t_d` is updated.
   - It also runs in \(O(n)\) time.
4. **Dictionary Comparison** (`return s_d == t_d`):
   - Comparing two dictionaries in Python is \(O(n)\) in the worst case, where \(n\) is the total number of keys in the dictionaries. Here, it's proportional to the number of unique characters in `s` or `t`.

**Overall Time Complexity**:  
- Since the loops are sequential (not nested), the total time complexity is:
  \[
  O(n) + O(n) + O(n) = O(n)
  \]

### Space Complexity
1. **Space for `s_d` and `t_d`**:
   - In the worst case, both `s` and `t` have all unique characters. Therefore, `s_d` and `t_d` will each store \(n\) key-value pairs, where \(n\) is the length of `s` or `t`.
   - The space used by each dictionary is \(O(n)\).
2. **Additional Variables**:
   - Variables like `char`, `s`, and `t` occupy \(O(1)\) space, which is constant.

**Overall Space Complexity**:
- Since we're using two dictionaries that each can store up to \(n\) elements, the overall space complexity is:
  \[
  O(n) + O(n) = O(n)
  \]

### Summary
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the strings `s` and `t`.
- **Space Complexity**: \(O(n)\), due to the storage in dictionaries `s_d` and `t_d`.
"""
