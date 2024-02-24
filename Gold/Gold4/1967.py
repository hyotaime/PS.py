# Python3 2% TLE, PyPy3 AC
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

rst = 0
for i in range(1, n + 1):
    stack = []
    visited = [False] * (n + 1)
    stack.append((i, 0))
    visited[i] = True
    while stack:
        x, w = stack.pop()
        for nx, nw in graph[x]:
            if not visited[nx]:
                stack.append((nx, w + nw))
                visited[nx] = True
                rst = max(rst, w + nw)
print(rst)
