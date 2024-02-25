import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n < 1:
        break
    cnt, rst = 0, 0
    for _ in range(n):
        s, t = map(int, input().split())
        rst += s * (t - cnt)
        cnt = t
    print(rst, 'miles')
