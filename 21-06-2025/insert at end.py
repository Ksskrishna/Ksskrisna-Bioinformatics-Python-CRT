def insert_end (self,data):
    new = Node(data)
    if not self.head:
        self.head = new
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new