import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    rst = 1
    for i in range(1, n):
        rst += i * 2
    print(n, '=>',  rst)
