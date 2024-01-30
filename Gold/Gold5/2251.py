import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
rst = set()

stack = [(0, 0, c)]
visited = [[False] * 201 for _ in range(201)]
visited[0][0] = True
while stack:
    x, y, z = stack.pop()
    if x == 0:
        rst.add(z)
    for nx, ny, nz in (x - b + y, b, z), (0, x + y, z), (x - c + z, y, c), (0, y, x + z), (a, y - a + x, z), (
            x + y, 0, z), (x, y - c + z, c), (x, 0, y + z), (a, y, z - a + x), (x + z, y, 0), (x, b, z - b + y), (
            x, y + z, 0):
        if 0 <= nx <= a and 0 <= ny <= b and 0 <= nz <= c and not visited[nx][ny]:
            visited[nx][ny] = True
            stack.append((nx, ny, nz))

print(*sorted(rst))
