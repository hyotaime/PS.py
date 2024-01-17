import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = [float('inf')] * (n+1)
visited = [False] * (n+1)
queue = deque([a])
cnt[a] = 0

node = [[] for _ in range(n+1)]

for i in range(n):
    for j in range(i+1-arr[i], 0, -arr[i]):
        node[i+1].append(j)
    for j in range(i+1+arr[i], n + 1, arr[i]):
        node[i+1].append(j)

while queue:
    now = queue.popleft()
    if visited[now]:
        continue
    visited[now] = True
    for i in node[now]:
        queue.append(i)
        cnt[i] = min(cnt[now] + 1, cnt[i])

print(cnt[b] if cnt[b] != float('inf') else -1)
