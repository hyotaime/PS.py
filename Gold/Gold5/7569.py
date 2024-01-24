import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
dir = [[0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz = z + dir[0][i]
        ny = y + dir[1][i]
        nx = x + dir[2][i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and tomato[nz][ny][nx] == 0:
            tomato[nz][ny][nx] = tomato[z][y][x] + 1
            queue.append((nz, ny, nx))

rst = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        rst = max(rst, max(j))
print(rst - 1)
