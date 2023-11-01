import sys

input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    rst = 0
    if n == 0 and m == 0:
        break
    arr = list(map(int, input().split()))
    for a in arr:
        if a > m//n:
            rst += m//n
        else:
            rst += a
    print(rst)
