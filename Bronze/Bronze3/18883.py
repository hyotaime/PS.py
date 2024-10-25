n, m = map(int, input().split())
i = 1
for _ in range(n):
    for _ in range(m - 1):
        print(i, end=' ')
        i += 1
    print(i)
    i += 1