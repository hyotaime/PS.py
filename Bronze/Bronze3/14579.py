a, b = map(int, input().split())
rst = 1
for i in range(a, b + 1):
    x = sum([j for j in range(i + 1)]) % 14579
    rst *= x
    rst %= 14579
print(rst)