import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([a])
visited = [False] * (n + 1)
visited[a] = True
cnt = 0
while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == b:
            print(cnt)
            exit()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    cnt += 1

print(-1)
