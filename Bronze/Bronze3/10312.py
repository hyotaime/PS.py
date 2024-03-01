import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    k = int(input())
    p = 0
    while 3 ** p <= k:
        p += 1
    p -= 1
    rst = []
    for i in range(p, -1, -1):
        rst.append(k // (3 ** i))
        k %= 3 ** i
    print(*rst)
