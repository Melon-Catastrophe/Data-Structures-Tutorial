from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)

print("Front of queue item:", q.popleft())
print("Queue:", q)