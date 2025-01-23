"""
    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
    """


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_s = {}
    freq_t = {}

    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1

    return freq_s == freq_t


"""
Time and Space Complexity
Time Complexity: 
O(n), where 
n is the length of the strings. This is because we iterate over both strings once to count characters.
Space Complexity: 
O(1) (considering only 26 lowercase English letters or 
O(k), where 
k is the number of unique characters).
"""
