import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

rst = []
max_cnt = 0
for i in range(1, n + 1):
    queue = deque([i])
    visited = [False] * (n + 1)
    visited[i] = True
    cnt = 0
    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if not visited[j]:
                visited[j] = True
                cnt += 1
                queue.append(j)
    if cnt > max_cnt:
        rst = [i]
        max_cnt = cnt
    elif cnt == max_cnt:
        rst.append(i)

print(*rst)
