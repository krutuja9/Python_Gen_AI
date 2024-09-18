# from collections import deque

# queue = deque()

# queue.append('a')
# queue.append("b")
# queue.append("c")

# print(queue.popleft())
# print(queue)

import queue
q = queue.Queue()
q.put("x")
q.put("y")
q.put("z")

print(q.get())
print(q.queue)