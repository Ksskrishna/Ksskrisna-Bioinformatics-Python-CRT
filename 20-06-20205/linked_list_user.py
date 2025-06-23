'''
create a linked list to take size n 
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n = int(input("enter the range of linked list: "))
values = int(input("enter the values in the list: "))
head = Node(values)
for i in range(n):
    values = Node(input("enter the element: "))
    head.next = Node(values)