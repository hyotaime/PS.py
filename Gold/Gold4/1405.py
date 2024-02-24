import sys

input = sys.stdin.readline
n, e_p, w_p, s_p, n_p, = map(int, input().split())
e_p, w_p, s_p, n_p = e_p / 100, w_p / 100, s_p / 100, n_p / 100

stack = [(0, 0, 0, 1, [(0, 0)])]
rst = 0.0
while stack:
    x, y, cnt, p, visited = stack.pop()
    if p == 0:
        continue
    if cnt == n:
        rst += p
        continue
    nx, ny = x + 1, y
    if (nx, ny) not in visited:
        stack.append((nx, ny, cnt + 1, p * e_p, visited + [(nx, ny)]))
    nx, ny = x - 1, y
    if (nx, ny) not in visited:
        stack.append((nx, ny, cnt + 1, p * w_p, visited + [(nx, ny)]))
    nx, ny = x, y + 1
    if (nx, ny) not in visited:
        stack.append((nx, ny, cnt + 1, p * s_p, visited + [(nx, ny)]))
    nx, ny = x, y - 1
    if (nx, ny) not in visited:
        stack.append((nx, ny, cnt + 1, p * n_p, visited + [(nx, ny)]))

print(rst)
