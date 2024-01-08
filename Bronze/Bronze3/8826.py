import sys

input = sys.stdin.readline
z = int(input())
for _ in range(z):
    n = int(input())
    a, b = 0, 0
    w = input().rstrip()
    for d in w:
        if d == 'E':
            a += 1
        elif d == 'W':
            a -= 1
        elif d == 'N':
            b += 1
        elif d == 'S':
            b -= 1
    print(abs(a) + abs(b))
