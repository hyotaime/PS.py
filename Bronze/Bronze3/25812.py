import sys

input = sys.stdin.readline
n, r = map(int, input().split())
a, b = 0, 0
for _ in range(n):
    cur = int(input())
    if cur == r:
        continue
    if cur < r:
        a += 1
    else:
        b += 1
if a == b:
    print(0)
elif a > b:
    print(1)
else:
    print(2)
