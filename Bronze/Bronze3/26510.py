import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
for n in arr:
    for i in range(n - 1):
        print(' ' * i, end='')
        print('*', end='')
        print(' ' * ((n - i) * 2 - 3), end='')
        print('*')
    print(' ' * (n - 1), end='')
    print('*')
