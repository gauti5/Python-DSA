# Stack Implementation

class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self, element):
        self.stack.append(element)
        print(f"element {element} added/pushed to the stack")
    
    def peek(self):
        if not self.is_empty():
            print(f"Peak element is {self.stack[-1]}")
        else:
            print("Stack is empty!!")
    
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if not self.is_empty():
            last_element=self.stack.pop()
            print(f"The element {last_element} is removed from stack")
        else:
            print("Stack is empty!!")
        

s=stack()
s.push(22)
s.push(23)
s.peek()
s.pop()
s.peek()