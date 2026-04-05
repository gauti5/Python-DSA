# Queue Implementation

class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self, val):
        self.queue.append(val)
        print(f"element {val} is added to the queue")
        
    def dequeue(self):
        if not self.is_empty():
            removed_element=self.queue.pop(0)
            print(f"element {removed_element} is removed from the queue")
        else:
            print("Queue is empty!!")
    
    def front(self):
        print(f"Top element in the Queue is {self.queue[0]}")
    
    def is_empty(self):
        return len(self.queue)==0
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(25)
q.front()
q.is_empty()