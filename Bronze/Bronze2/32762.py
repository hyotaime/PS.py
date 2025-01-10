n, m = map(int, input().split())
for _ in range(n):
    s, e = map(int, input().split())

rst = 0
for _ in range(m):
    t, p = map(int, input().split())
    rst += p

print(rst / n)
