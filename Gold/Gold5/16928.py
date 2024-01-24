import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
    a, b = map(int, input().split())
    d[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    d[a] = b

queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    x, cnt = queue.popleft()
    if x == 100:
        print(cnt)
        break
    for i in range(1, 7):
        nx = x + i
        if nx <= 100 and not visited[nx]:
            if nx in d:
                nx = d[nx]
            queue.append((nx, cnt + 1))
            visited[nx] = True
