"""
Stacks follow the principle of Last in First Out -->  LIFO

we can perform this operations using built python list using methods like Append and Pop

but differences are : 
 1. conceptual diff : list is for genearal purpose where stack is meant to do for LIFO 
 list allows accessing elements , removing at any position, lists are not necessarily only used for LIFO principle
list allows insertions at any positions as well , when we insert at 0 the whole indexing changes which is again a O(n) 
operation 

2. Stack are effecient ,when implemented using list as they only allow append and pop methods.
which is O(1) operation 

while for List appending and popping is O(1) but inserting and removing are O(n)

"""
from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def is_empty(self):
        return True if len(self.stack) == 0  else False
    
    def append(self,ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def display(self):
        return self.stack

    def peek(self):
        return self.stack[-1]
    
if __name__ == '__main__':
    stack = Stack()
    stack.append(10)
    stack.append(9)
    print(stack.display())
    print(stack.peek())
    stack.pop()
    print(stack.display())