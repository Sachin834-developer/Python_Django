class Node:
    def __init__(self,prev,next,data) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_last_node(self) -> Node:
        node  = self.head
        while node.next:
            node = node.next
        return node
    
    def get_length(self):
        if self.head is None:
            return 0
        
        node = self.head
        count =0 
        while node:
            count+=1
            node=node.next
        return count

    def print_forward(self):
        if self.head is None:
            print('Doubly Linked list is empty')
            return

        node  = self.head
        dll_str = ''
        while node:
            dll_str+=str(node.data) + '-->'
            node = node.next
        print(dll_str)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        node = self.get_last_node()
        dll_str = ''
        while node:
            dll_str+=str(node.data) + '<--'
            node = node.prev
        print(dll_str)

    def insert_at_beginning(self,data):
        node = Node(None,self.head,data)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(None,None,data)
            return
        
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(node,None,data)

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        node = self.head
        counter = 0
        while node:
            if counter == index-1:
                new_node =Node(node,node.next,data)
                node.next = new_node
                if new_node.next:
                    new_node.next.prev = new_node
            counter +=1
            node = node.next

    def remove_at(self,index):
        if index>0 and index>=self.get_length():
            raise Exception('Invalid Input')
        
        if index==0:
            self.head =self.head.next
            self.head.prev = None
            return

        node = self.head
        count =0
        while node:
            if count == index:
                node.prev = node.next
                if node.next:
                    node.next.prev = node.prev
                break
            node = node.next
            count+=1
        
    def insert_values(self,data_list): 
        self.head = None
        for value in data_list: 
            self.insert_at_end(value)

    def delete_node(node_to_delete): # 0(1)
        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev


if __name__=='__main__':
    dll = DoubleLinkedList()
    # dll.insert_at_beginning(1)
    # dll.insert_at_beginning(2)
    # dll.insert_at_end(4)
    # dll.insert_at_beginning(3)
    # dll.insert_at(2,'two')
    # dll.insert_at(5,'t')
    # dll.print_forward()
    # dll.print_backward()
    # dll.remove_at(5)
    # dll.remove_at(0)
    # print(dll.get_length())
    dll.insert_values([1,2,3,4,5])
    dll.print_forward()
    dll.print_backward()