from collections import deque
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueing: ", queue)
first = queue.popleft()
print("Dequeued element : ",first)
print("Queue after dequeing: ", queue)
if not queue:
    print("queue is empty")
else:
    print("queue is not empty")
print("front element: ", queue)