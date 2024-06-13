from collections import deque


def bfs(i, j):
    united = [(i, j)]
    q = deque([(i, j)])
    visited[i][j] = True
    sum = graph[i][j]
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if L <= abs(graph[nr][nc] - graph[r][c]) <= R:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    sum += graph[nr][nc]
                    united.append((nr, nc))
    if len(united) > 1:
        for i, j in united:
            graph[i][j] = sum // len(united)
        return True
    return False


n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

rst = 0
while True:
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    cnt += 1
    if cnt == 0:
        break

    rst += 1

print(rst)
