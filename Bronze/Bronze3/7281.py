import sys

input = sys.stdin.readline
n = int(input())
tmp, rst = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if b == 1:
        rst = max(rst, a - tmp)
        tmp = a
print(rst)
