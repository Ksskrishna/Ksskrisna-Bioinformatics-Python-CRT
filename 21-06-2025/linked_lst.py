class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    def insert_front(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

L1 = Linked_list()
L1.insert_front(5)
L1.insert_front(15)
L1.insert_front(20)
L1.show()