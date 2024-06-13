from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
shark = (0, 0)
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark = (i, j)
            space[i][j] = 0
            break
size = 2
eat = 0
t = 0
while True:
    q = deque([(0, shark[0], shark[1])])
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True
    fish = []
    while q:
        d, r, c = q.popleft()
        if 0 < space[r][c] < size:
            fish.append((d, r, c))
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and space[nr][nc] <= size:
                visited[nr][nc] = True
                q.append((d + 1, nr, nc))
    if not fish:
        break
    fish.sort()
    d, r, c = fish[0]
    space[r][c] = 0
    shark = (r, c)
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    t += d
print(t)
