n = int(input())
x, y = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        x += a
        y += b
    elif a > b:
        x += a + b
    else:
        y += a + b
print(x, y)
