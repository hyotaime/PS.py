from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

rst = 0
while True:
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                flag = True
                break
    if not flag:
        print(rst)
        exit()

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    cnt = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if graph[nr][nc] == 1:
                    cnt[nr][nc] += 1
                else:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
    for i in range(n):
        for j in range(m):
            if cnt[i][j] >= 2:
                graph[i][j] = 0
    rst += 1
