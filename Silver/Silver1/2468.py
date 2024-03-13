import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
rst = 0
for k in range(101):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] < k:
                visited[i][j] = True
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
    rst = max(rst, cnt)

print(rst)
