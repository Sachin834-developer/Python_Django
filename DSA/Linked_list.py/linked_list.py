"""

1. Dynamic Size
Linked List: Linked lists are dynamic in size, meaning they can easily grow or shrink in memory. You can insert or delete nodes without worrying about reallocating or resizing.

Array: Arrays have a fixed size. If the array is full, you need to create a larger array and copy the elements over, which can be time-consuming.

2. Efficient Insertions and Deletions
Linked List: Inserting or deleting elements in a linked list can be more efficient, especially if you already have a reference to the insertion or deletion point. This operation is 
O(1) if you have direct access to the node.

Array: Inserting or deleting elements in an array can be costly because you may need to shift elements to maintain order. This operation is 
O(n) in the worst case.

When to Use Linked Lists Over Arrays:

When you need a data structure with a dynamic size.
When your application frequently inserts or deletes elements, especially from the middle of the list.
When memory efficiency is a concern, and you want to avoid the overhead of resizing arrays.
When implementing complex data structures that require flexible node management.


Trade-Offs
While linked lists have these advantages, they also come with some trade-offs:

Access Time: Accessing an element by index in a linked list is O(n) because you need to traverse the list from the head. In contrast, arrays offer O(1) access time.
Memory Overhead: Linked lists use extra memory for storing pointers/references in each node, which can be significant for large datasets.
Choosing between linked lists and arrays depends on the specific requirements of the task, such as the need for random access versus dynamic resizing and frequent insertions/deletions.


"""
num_list = list(range(6,11)) # [i for i in range(5)]

class Node:
    def __init__(self,data:any,next_node:object) -> None:
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self) -> None:
        self.top_node = None

    def print(self) -> None:
        if self.top_node is None:
            print("Linked List is Empty")

        cur_node = self.top_node
        str_rep =''
        while cur_node:
            str_rep += str(cur_node.data)  + '-->'
            cur_node = cur_node.next
        print(str_rep)

    def insert_at_beginning(self,element:any) -> None:
        node = Node(element,self.top_node)
        self.top_node = node

    def insert_at_end(self,element:any) -> None:
        node = Node(element,None)
        if self.top_node is None:
            self.top_node = node
            return

        top_node = self.top_node
        while top_node.next:
            top_node = top_node.next

        top_node.next = node
    
    def insert_values(self,data_list:list) -> None:
        # take list of values and create a new fresh linked list
        self.top_node = None

        for value in data_list:
            self.insert_at_end(value)
            # self.insert_at_beginning(value)

    def get_length(self) -> int:
        counter = 0
        top_node  = self.top_node
        while top_node:
            top_node = top_node.next
            counter+=1
        return counter
    
    def remove_at(self,index:int) -> None:

        if index<0 or index>=self.get_length():#because index starts at 0
            raise Exception('Invalid input')
        
        if index == 0:
            self.top_node = self.top_node.next

        counter = 0
        current_node = self.top_node
        while current_node:
            if counter==index-1:
                current_node.next = current_node.next.next #current_node.next is the removing element so we take next from removing el and keep it to its previos el
                break
            current_node = current_node.next
            counter+=1

    def insert_at(self,index:int,data:any) -> None:

        if 0<index>self.get_length():
            raise Exception('Invalid Input index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        counter = 0
        cur_node = self.top_node

        while cur_node:
            if counter==index-1:
                cur_node.next = Node(data,cur_node.next)
                break
            cur_node = cur_node.next
            counter+=1

    def inser_after_this_value(self,data_after:any,data:any) -> None:
        if self.top_node is None:
                return
        
        cur_node  = self.top_node
        while cur_node:
            if cur_node.data == data_after:
                cur_node.next = Node(data,cur_node.next)
                break
            elif cur_node.next is None:
                raise Exception('Invalid Input:',data_after)
            cur_node = cur_node.next

    def remove_by_this_value(self, data:any) -> None: #O(n)  traversal to find 
            # Remove first node that contains 
            if self.top_node is None:
                return
            
            if self.top_node.data == data:
                self.top_node = self.top_node.next

            cur_node  = self.top_node
            while cur_node.next:
                if cur_node.data == data:
                    cur_node.next = cur_node.next.next
                    break
                cur_node = cur_node.next

    def delete_node(prev_node): #  O(1) bcoz we have referenve node
        if prev_node and prev_node.next:
            prev_node.next = prev_node.next.next  # Bypass the node to be deleted


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning('a')
    # ll.insert_at_end(4)
    # ll.insert_at_end(5)
    # ll.insert_values(num_list)
    # ll.print()
    # # ll.inser_after_this_value(6,'six')
    # # ll.inser_after_this_value(0,'11')
    # ll.remove_by_this_value(7)
    # ll.remove_by_this_value(10)
    # ll.remove_by_this_value(6)
    # ll.remove_by_this_value(9)
    # ll.remove_by_this_value(8)
    
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.inser_after_this_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_this_value("orange") # remove orange from linked list
    ll.print()
    # ll.remove_by_this_value("figs")
    ll.remove_by_this_value("banana")
    ll.print()
    ll.remove_by_this_value("mango")
    ll.remove_by_this_value("apple")
    ll.remove_by_this_value("grapes")
    ll.print()


    # ll.remove_at(2)
    # ll.insert_at(2,'seven')
    # ll.insert_at(4,'eight')
    # print(ll.get_length())
    # ll.remove_at(2)

    ll.print()



    