n, l, d = map(int, input().split())
rst = 0
for i in range(n - 1):
    rst += l
    if rst % d == 0:
        break
    rst += 1
    if rst % d == 0:
        break
    rst += 1
    if rst % d == 0:
        break
    rst += 1
    if rst % d == 0:
        break
    rst += 1
    if rst % d == 0:
        break
    rst += 1
else:
    rst += l
    rst = ((rst - 1) // d + 1) * d

print(rst)
