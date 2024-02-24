import sys

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

stack = {(0, 0, 1, board[0][0])}
rst = 0
while stack:
    cr, cc, cnt, visited = stack.pop()
    if cnt > rst:
        rst = cnt
    for dr, dc in dir:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < r and 0 <= nc < c and board[nr][nc] not in visited:
            stack.add((nr, nc, cnt + 1, visited + board[nr][nc]))
print(rst)
