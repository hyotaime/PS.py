import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    m -= 45
    if m < 0:
        h -= 1
        m += 60
    if h < 0:
        h += 24
    print(f'Case #{i + 1}: {h} {m}')
