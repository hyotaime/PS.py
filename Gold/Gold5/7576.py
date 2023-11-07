import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

cnt = 0
while q:
    r, c = q.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            q.append((nr, nc))

for i in range(n):
    cnt = max(cnt, max(box[i]))
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            sys.exit(0)
print(cnt - 1)
