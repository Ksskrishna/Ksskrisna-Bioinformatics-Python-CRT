class Stack:
    def __init__(self):
        self.Stack = [] 
        print("Object created")

    def push(self, element):
        self.Stack.append(element)
        print(f"Element {element} is added")

    def pop(self):
        if not self.Stack:
            print("Stack is empty")
        else:
            removed = self.Stack.pop()
            print(f"Element {removed} is removed")

    def peek(self):
        if not self.Stack:
            print("Stack is empty")
        else:
            print(f"Peek element is {self.Stack[-1]}")

    def display(self):
        str = []
        for i in self.Stack:
            str.append(i)
            i = "".join(str)
        print(i)


    def length(self):
        print(f"Length of the stack is: {len(self.Stack)}")

stack = Stack()
stack.push(105)
stack.push(210)
stack.display()
stack.peek()
stack.length()
stack.pop()
stack.display()
