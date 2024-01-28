import sys

input = sys.stdin.readline
n, m= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

stack = []
visited = [[False] * m for _ in range(n)]
cnt = 0
msize = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            stack.append((i, j))
            visited[i][j] = True
            size = 1
            cnt += 1
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and not visited[nr][nc]:
                        stack.append((nr, nc))
                        visited[nr][nc] = True
                        size += 1
            msize = max(msize, size)

print(cnt)
print(msize)
