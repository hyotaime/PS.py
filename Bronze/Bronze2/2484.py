n = int(input())
m = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    tmp = 0
    if a == b == c == d:
        tmp = 50000 + a * 5000
    elif a == b == c:
        tmp = 10000 + a * 1000
    elif a == b == d:
        tmp = 10000 + a * 1000
    elif a == c == d:
        tmp = 10000 + a * 1000
    elif b == c == d:
        tmp = 10000 + b * 1000
    elif a == b and c == d:
        tmp = 2000 + a * 500 + c * 500
    elif a == c and b == d:
        tmp = 2000 + a * 500 + c * 500
    elif a == b:
        tmp = 1000 + a * 100
    elif a == c:
        tmp = 1000 + a * 100
    elif a == d:
        tmp = 1000 + a * 100
    elif b == c:
        tmp = 1000 + b * 100
    elif b == d:
        tmp = 1000 + b * 100
    elif c == d:
        tmp = 1000 + c * 100
    else:
        tmp = max([a, b, c, d]) * 100
    m = max(m, tmp)

print(m)