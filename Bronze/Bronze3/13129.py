a, b, n = map(int, input().split())
rst = []
for i in range(1, n + 1):
    rst.append(a * n + b * i)

print(*rst)