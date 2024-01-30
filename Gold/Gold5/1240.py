import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

for _ in range(m):
    a, b = map(int, input().split())
    visited = [False] * (n + 1)
    visited[a] = True
    queue = deque([(a, 0)])
    while queue:
        x, w = queue.popleft()
        if x == b:
            print(w)
            break
        for nx, nw in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx, w + nw))
