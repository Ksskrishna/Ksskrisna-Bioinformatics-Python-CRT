'''
write a py prog to take length of queue to take input from user and add elments using enqueue method 
and print the elements present in the queue and remove the elements one by one from the queue 
and check weather the queue is emptty or not and print the front peek and rear peak 
'''
class Queue():
    def __init__(self):
        self.length = int(input("enter the length of queue: "))
        self.que = []
    def queue(self):
        for i in range(self.length):
            temp = input(f"enter element {i} in the queue: ")
            self.que.append(temp)
        print(self.que)

    def peek_front(self):
        length = len(self.que)
        if length == 0:
            print("None")
        else:
            print(f"peak front of the queue is: {self.que[0]}")

    def peek_rear(self):
        length = len(self.que)
        if length == 0:
            print("None")
        else:
            print(f"peak rear of the queue is: {self.que[-1]}")

    def remove(self):
        if self.que:
            removed = self.que.pop(0)
        print(removed)
    
    def empty(self):
        length = len(self.que)
        if length == 0:
            print("empty queue")
        else:
            print(f"queue had elements: {self.que}")

O1 = Queue()
O1.queue()
O1.peek_front()
O1.peek_rear()
O1.remove()
O1.remove()
O1.remove()
O1.remove()
O1.remove()
O1.empty()