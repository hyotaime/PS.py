import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
link = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
for i in range(1, n + 1):
    link[i].sort()
cnt = 1
deque = deque([r])
while deque:
    x = deque.popleft()
    if visited[x] == 0:
        visited[x] = cnt
        cnt += 1
        deque.extend(link[x])
for i in range(1, n + 1):
    print(visited[i])
