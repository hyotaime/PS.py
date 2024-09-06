n = int(input())
m = int(input())
rst = m
for _ in range(n):
    a, b = map(int, input().split())
    m = m + a - b
    if m < 0:
        print(0)
        break
    rst = max(rst, m)
else:
    print(rst)
