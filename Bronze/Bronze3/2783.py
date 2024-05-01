x, y = map(int, input().split())
rst = 1000 / y * x
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    rst = min(rst, 1000 / b * a)
print(rst)
