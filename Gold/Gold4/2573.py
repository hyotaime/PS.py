# Python TLE, PyPy3 AC
import sys

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

rst = 0
flag = True
while flag:
    flag = False
    rst += 1
    arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                flag = True
                cnt = 0
                for dr, dc in dir:
                    nr, nc = i + dr, j + dc
                    if board[nr][nc] == 0:
                        cnt += 1
                arr[i][j] = cnt
    for i in range(r):
        for j in range(c):
            board[i][j] -= arr[i][j]
            if board[i][j] < 0:
                board[i][j] = 0
    visited = [[False] * c for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                cnt += 1
                if cnt > 1 and not visited[i][j]:
                    print(rst)
                    exit(0)
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in dir:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < r and 0 <= nc < c and board[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))

print(0)
