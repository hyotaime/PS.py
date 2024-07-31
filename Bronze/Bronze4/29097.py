n, m, k, a, b, c = map(int, input().split())
mx = max(n * a, m * b, k * c)
rst = []
if mx == n * a:
    rst.append("Joffrey")
if mx == m * b:
    rst.append("Robb")
if mx == k * c:
    rst.append("Stannis")
print(*rst)
