import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

stack = []

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            stack.append((i, j))
        while stack:
            r, c = stack.pop()
            visited[r][c] = True
            if board[r][c] == '-':
                if c + 1 < m and board[r][c + 1] == '-' and not visited[r][c + 1]:
                    stack.append((r, c + 1))
                else:
                    cnt += 1
            elif board[r][c] == '|':
                if r + 1 < n and board[r + 1][c] == '|' and not visited[r + 1][c]:
                    stack.append((r + 1, c))
                else:
                    cnt += 1

print(cnt)
