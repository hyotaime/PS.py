import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start = ()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start = (i, j)
            break
q = deque()
q.append(start)
arr[start[0]][start[1]] = 1
while q:
    r, c = q.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
            arr[nr][nc] = arr[r][c] + 1
            q.append((nr, nc))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = -1
        elif arr[i][j] != 0:
            arr[i][j] -= 1
arr[start[0]][start[1]] = 0
for i in range(n):
    print(*arr[i])
