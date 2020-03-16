from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append("하이")

print(len(queue))

print(queue)
print(queue[0])
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)
