from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]

queue = deque([(0, 0, False, 0)])
visited = [[False] * m for _ in range(n)]
visited_with_wall = [[False] * m for _ in range(n)]
visited[0][0] = True
while queue:
    r, c, wall, cnt = queue.popleft()
    if r == n - 1 and c == m - 1:
        print(cnt + 1)
        exit()
    if wall:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited_with_wall[nr][nc]:
                    if graph[nr][nc] == '0':
                        visited_with_wall[nr][nc] = True
                        queue.append((nr, nc, wall, cnt + 1))
    else:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    if graph[nr][nc] == '0':
                        visited[nr][nc] = True
                        queue.append((nr, nc, wall, cnt + 1))
                    elif not wall:
                        visited_with_wall[nr][nc] = True
                        queue.append((nr, nc, True, cnt + 1))
print(-1)
