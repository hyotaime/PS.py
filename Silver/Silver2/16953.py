import sys
from collections import deque

input = sys.stdin.readline
a, b = map(int, input().split())

queue = deque([a])
cnt = 0

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == b:
            print(cnt + 1)
            exit()
        if x < b:
            queue.append(x * 2)
            queue.append(x * 10 + 1)
    cnt += 1
print(-1)

