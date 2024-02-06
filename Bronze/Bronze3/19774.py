import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = input().rstrip()
    a, b, c, d = n[0], n[1], n[2], n[3]
    if (int(a + b) ** 2 + int(c + d) ** 2) % 7 == 1:
        print('YES')
    else:
        print('NO')
