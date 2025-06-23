class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    #insert at front
    def addnode(self,data):
        n_node = Node(data)
        n_node.next = self.head
        self.head = n_node
    #display at ned
    def display(self):
        current = self.head
        while current:
            print(current.data,end = " -> ")
            current = current.next
        print("None")
    #insert at end
    def insert_end (self,data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
    #count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    #delting the first node
    def delete_node(self):
        if self.head:
            self.head = self.head.next

L1 = Linked_list()
L1.addnode(25.69)
L1.addnode(27.2)
L1.addnode(55.54)
L1.addnode(22.41)
L1.display()
