import heapq
import time

employees = [1001, 1002, 1003, 1004]

tasks = [i for i in range(99)]

q = [[0, 0, i] for i in employees]

heapq.heapify(q)

for task in tasks:
    time.sleep(1/10)
    v = heapq.heappop(q)
    v[0] += 1
    v[1] = int(time.time())
    heapq.heappush(q, v)

print(q)
