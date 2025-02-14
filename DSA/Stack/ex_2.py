"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def is_match(char):
            if char == ')':
                return stack.pop() == '('
            elif char == '}':
                return stack.pop() == '{'
            elif char == ']':
                return stack.pop() == '['
            
        for char in s:
            if char in ('(','{','['):
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                if not is_match(char):
                    return False
        return True if len(stack) <= 0 else False

    
    





        