import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
stack = [1]

while stack:
    x = stack.pop()
    for i in graph[x]:
        if not visited[i]:
            parent[i] = x
            stack.append(i)
            visited[i] = True


for i in range(2, n + 1):
    print(parent[i])
