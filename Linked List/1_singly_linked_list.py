class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked List is empty!!")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next 
                
    def add_begin(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def add_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            
    def add_after(self, data, X):
        temp=self.head
        while temp is not None:
            if X==temp.data:
                break
            temp=temp.next
            
        if temp is None:
            print("Node is not present in linked list")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node
            
    def add_before(self, data, X):
        if self.head is None:
            print('Linked list is empty')
            
        if self.head.data==X:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        n=self.head
        while n.next is not None:
            if n.next.data==X:
                break
            n=n.next
            
        if n.next is None:
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
            
    def insert_empty(self,data):
        if self.data is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is not empty!!")
            
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty cant delete")
        else:
            self.head=self.head.next
            
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty cant delete")
        elif self.head.next is None:
            self.head=None
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
            
    def delete_any(self, X):
        if self.head is None:
            print("Linked list is empty cant delete")
            return 
        
        if self.head.data==X:
            self.head=self.head.next
            return 
        
        n=self.head
        while n.next is not None:
            if n.next.data==X:
                break
            n=n.next
        if n.next is None:
            print("Node is not present")
        else:
            n.next=n.next.next 
            
LL=SinglyLinkedList()
LL.add_begin(10)
LL.add_after(200,10)
LL.add_end(100)
LL.add_begin(20)
LL.add_after(20,10)
LL.add_before(10,10)
LL.delete_begin()
LL.delete_last()
LL.delete_any(200)
LL.display()
    