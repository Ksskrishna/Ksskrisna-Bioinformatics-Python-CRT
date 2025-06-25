class Stack():
    def __init__(self):
        self.Stack = [] 
        print("Object created")

    def push(self, element):
        self.Stack.append(element)
        print(f"Element {element} is added")
    def check_balance(self):
        if self.Stack[0:3] == self.Stack[:3]:
            print("balanced")
        else:
            print("immbalanced")

stack = Stack()
stack.push('([{}])')
stack.push('{([])}')
stack.check_balance('{([])}')