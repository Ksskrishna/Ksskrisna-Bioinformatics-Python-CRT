from collections import deque
stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print(f"Stack after pushing {stack}")
top = stack.pop()
print("popped element: ",top)
print("stack after ")


