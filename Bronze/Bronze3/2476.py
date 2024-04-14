n = int(input())
rst = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        rst = max(rst, 10000 + a * 1000)
    elif a == b or a == c:
        rst = max(rst, 1000 + a * 100)
    elif b == c:
        rst = max(rst, 1000 + b * 100)
    else:
        rst = max(rst, max(a, b, c) * 100)
print(rst)
