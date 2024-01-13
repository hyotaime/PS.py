import sys

input = sys.stdin.readline
n = int(input())
h, m, s = 0, 0, 0
for _ in range(n):
    a, b = map(int, input().split(':'))
    m += a
    s += b
    if s >= 60:
        m += 1
        s -= 60
    if m >= 60:
        h += 1
        m -= 60
print(f'{h:02}:{m:02}:{s:02}')
