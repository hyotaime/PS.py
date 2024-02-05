import sys

input = sys.stdin.readline
t = int(input())
a, b, c = 0, 0, 0
for _ in range(t):
    na, nb, nc = map(int, input().split())
    a += na
    b += nb
    c += nc
    if a >= 30 and b >= 30 and c >= 30:
        rst = min(a, b, c)
        print(rst)
        a -= rst
        b -= rst
        c -= rst
    else:
        print('NO')
