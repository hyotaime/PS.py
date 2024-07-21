t = int(input())
for _ in range(t):
    n = int(input())
    print(f'Pairs for {n}: ', end='')
    for i in range(1, n // 2 + 1):
        if i != n - i:
            print(f'{i} {n - i}', end='')
        if n - 2 * i > 2:
            print(', ', end='')
    print()

