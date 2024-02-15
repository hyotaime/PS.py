# Python TLE, PyPy3 AC
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
dir = [(0, 1), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
cnt = 0
start = (0, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'F':
            start = (i, j)
            break

queue = deque([start])
while queue:
    r, c = queue.popleft()
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == '.':
            queue.append((nr, nc))
            graph[nr][nc] = 'O'
            cnt += 1
print(cnt)
