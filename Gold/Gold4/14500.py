import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rst = 0
# TLE
# maxx = max([max(i) for i in arr])
# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# for i in range(n):
#     for j in range(m):
#         visited = [[False] * m for _ in range(n)]
#         visited[i][j] = True
#         stack = [(i, j, 1, arr[i][j])]
#         while stack:
#             r, c, chk, cnt, = stack.pop()
#             if chk == 4:
#                 rst = max(rst, cnt)
#                 continue
#             # 나머지 블록들이 최대여도 rst보다 작으면 더 계산할 필요가 없음.
#             if rst > cnt + maxx * (4 - chk):
#                 continue
#             for dr, dc in d:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
#                     visited[nr][nc] = True
#                     stack.append((nr, nc, chk + 1, cnt + arr[nr][nc]))
#
#         if i > 0 and 0 < j < m - 1:
#             rst = max(rst, arr[i][j] + arr[i - 1][j] + arr[i][j - 1] + arr[i][j + 1])
#         if 0 < i < n - 1 and j < m - 1:
#             rst = max(rst, arr[i][j] + arr[i - 1][j] + arr[i + 1][j] + arr[i][j + 1])
#         if i < n - 1 and 0 < j < m - 1:
#             rst = max(rst, arr[i][j] + arr[i + 1][j] + arr[i][j - 1] + arr[i][j + 1])
#         if 0 < i < n - 1 and j > 0:
#             rst = max(rst, arr[i][j] + arr[i - 1][j] + arr[i + 1][j] + arr[i][j - 1])
#
# print(rst)

# Bruteforce
tetris = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (1, 0), (0, 1), (1, 1)],
          [(0, 0), (1, 0), (2, 0), (2, 1)],
          [(0, 1), (1, 1), (2, 1), (2, 0)],
          [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (0, 1), (1, 0), (2, 0)],
          [(0, 0), (1, 0), (1, 1), (1, 2)],
          [(0, 2), (1, 1), (1, 2), (1, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)],
          [(0, 0), (1, 0), (0, 1), (0, 2)],
          [(0, 0), (1, 0), (1, 1), (2, 1)],
          [(0, 1), (1, 1), (1, 0), (2, 0)],
          [(1, 0), (1, 1), (0, 1), (0, 2)],
          [(0, 0), (0, 1), (1, 1), (1, 2)],
          [(0, 1), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (1, 0), (1, 1), (2, 0)],
          [(0, 1), (1, 1), (1, 0), (2, 1)]]

for i in range(n):
    for j in range(m):
        for k in tetris:
            chk = True
            for a, b in k:
                if not (0 <= i + a < n and 0 <= j + b < m):
                    chk = False
                    break
            if chk:
                rst = max(rst, sum([arr[i + a][j + b] for a, b in k]))

print(rst)
