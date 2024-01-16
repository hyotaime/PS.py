import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
campus = [input().rstrip() for _ in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
rst = 0
visited = [[False] * m for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            queue.append((i, j))
            break

while queue:
    r, c = queue.popleft()
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if campus[nr][nc] == 'O' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
            if campus[nr][nc] == 'P' and not visited[nr][nc]:
                rst += 1
                visited[nr][nc] = True
                queue.append((nr, nc))

print(rst if rst else 'TT')
