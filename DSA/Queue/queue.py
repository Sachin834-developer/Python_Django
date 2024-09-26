from collections import deque

class Queue:

    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self,val):
        self.queue.appendleft(val)

    def dequeue(self):
        self.queue.pop()

    def display(self):
        return self.queue
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return True if len(self.queue) == 0 else False
    
    def peek(self):
        return self.queue[-1]
    
if __name__=='__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(9)
    print(queue.display())
    print(queue.peek())
    queue.dequeue()
    print(queue.display())

