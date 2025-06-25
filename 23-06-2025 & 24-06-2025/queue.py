class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.is_empty[-1]
    def size(self):
        return len(self.items)