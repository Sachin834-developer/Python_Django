# 5th june 2024 1st round
"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcdxyzxb"
Output: 7
Explanation: The answer is "abcdxyz", with the length of 7.
Example 2:
Input: s = "abcdabcbbxyzt"
Output: 5
Explanation: The answer is "bxyzt", with the length of 5.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

s = "pwwkew"
n = len(s)
max = 0
for i in range(n):
    substr = s[i]
    count = 1
    for j in range(i + 1, n):
        if s[j] in substr:
            break
        else:
            substr += s[j]
            count += 1
    if max < count:
        max = count

print(max)
