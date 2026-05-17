#Queue untuk Antrian Mahasiswa
from collections import deque
queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")
print("antrian:", list(queue))

queue.popleft()
print("setelah dilayani:", list (queue))