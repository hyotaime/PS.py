import sys
from copy import deepcopy

input = sys.stdin.readline
n = int(input())
arr1 = [list(map(str, input().rstrip())) for _ in range(n)]
arr2 = deepcopy(arr1)
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
a, b = 0, 0

for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

stack = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            stack.append((i, j))
            while stack:
                r, c = stack.pop()
                visited[r][c] = True
                for k in range(4):
                    nr = r + d[k][0]
                    nc = c + d[k][1]
                    if 0 <= nr < n and 0 <= nc < n and arr1[nr][nc] == arr1[r][c] and not visited[nr][nc]:
                        stack.append((nr, nc))
            a += 1

stack = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            stack.append((i, j))
            while stack:
                r, c = stack.pop()
                visited[r][c] = True
                for k in range(4):
                    nr = r + d[k][0]
                    nc = c + d[k][1]
                    if 0 <= nr < n and 0 <= nc < n and arr2[nr][nc] == arr2[r][c] and not visited[nr][nc]:
                        stack.append((nr, nc))
            b += 1

print(a, b)
