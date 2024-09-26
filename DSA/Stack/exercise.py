"""
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

"""
from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def is_empty(self):
        return True if len(self.stack) == 0  else False
    
    def push(self,ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def display(self):
        return self.stack

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
if __name__ == '__main__':
    stack = Stack()
    str_1='We will conquere COVID-19'
    for char in str_1:
        stack.push(char)
    res=''
    while stack.size()!=0:
        res+=stack.pop()
    print(str_1)
    print(res)   

    