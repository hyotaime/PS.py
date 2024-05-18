t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n + 1):
        if n & (1 << i):
            print(i, end=' ')
    print()
