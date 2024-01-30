import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

rst = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            is_peak = True
            visited[i][j] = True
            stack = [(i, j)]
            while stack:
                r, c, = stack.pop()
                for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        if arr[nr][nc] > arr[r][c]:
                            is_peak = False
                        if not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
            if is_peak:
                rst += 1

print(rst)
