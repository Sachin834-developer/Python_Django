s = "babad"
# Given a string s, return the longest palindromic substring in s.
"""
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
    """


def find_longest_palindromic_substr(string):
    longest = 0
    for i in range(len(string)):
        # odd length palindrome
        pal1 = expand_around_center(string, i, i)
        # even length palindrome
        pal2 = expand_around_center(string, i, i + 1)

        longest = max(len(pal1), longest)
        longest = max(len(pal2), longest)

    return longest


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


print(find_longest_palindromic_substr(s))
