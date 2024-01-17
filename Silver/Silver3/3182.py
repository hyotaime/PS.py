import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    graph[i].append(a - 1)

stack = [0]
rst = []

for i in range(n):
    cnt = 1
    visited = [False] * n
    visited[i] = True
    stack.append(i)
    while stack:
        x = stack.pop()
        for j in graph[x]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True
                cnt += 1
    rst.append(cnt)

print(rst.index(max(rst)) + 1)
