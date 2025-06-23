class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print("Element is appended.")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print("Element is Removed")
    def display(self):
        print(self.Stack)
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.pop()
stack.display()