import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    if arr[i] == -1:
        continue
    graph[arr[i]].append(i)

r = int(input())
rst = 0
visited = [False] * n

visited[r] = True
stack = [r]
while stack:
    r = stack.pop()
    for i in range(n):
        if r in graph[i]:
            graph[i].remove(r)
    for nr in graph[r]:
        if not visited[nr]:
            visited[nr] = True
            stack.append(nr)

for i in range(n):
    if not graph[i] and not visited[i]:
        rst += 1
print(rst)
