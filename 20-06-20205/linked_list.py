class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
first = Node(10)
seacond = Node(20)
third = Node(30)
forth = Node(50)
fifth = Node(60)
sixth = Node(70)
head = first
head.next = seacond
seacond.next = third
third.next = forth
forth.next = fifth
fifth.next = sixth

current = head
while current:
    print(current.data,end = "->")
    current = current.next
print("None")

