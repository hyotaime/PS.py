import sys

input = sys.stdin.readline
while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    print(min(c * 30 + d * 40, c * 35 + d * 30, c * 40 + d * 20))
