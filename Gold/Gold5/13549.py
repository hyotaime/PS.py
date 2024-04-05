import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
rst = float('inf')
queue = deque([(n, 0)])
visited = [False] * 100001
while queue:
    n, cnt = queue.popleft()
    if n == k:
        rst = min(rst, cnt)
    if 0 <= n * 2 <= 100000 and not visited[n * 2]:
        visited[n * 2] = True
        queue.append((n * 2, cnt))
    if 0 <= n - 1 <= 100000 and not visited[n - 1]:
        visited[n - 1] = True
        queue.append((n - 1, cnt + 1))
    if 0 <= n + 1 <= 100000 and not visited[n + 1]:
        visited[n + 1] = True
        queue.append((n + 1, cnt + 1,))

print(rst)
