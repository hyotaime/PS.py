n = int(input())
m = 0
arr = []
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if a == "pig":
        m = max(m, b)
    else:
        arr.append((a, b))

rst = m

for a, b in arr:
    if b < m:
        rst += b

print(rst)
