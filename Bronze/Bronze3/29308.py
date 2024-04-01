n = int(input())
m = 0
rst = ""
for _ in range(n):
    a, b, c = map(str, input().split())
    a = int(a)
    if c == "Russia" and a > m:
        m = a
        rst = b
print(rst)
