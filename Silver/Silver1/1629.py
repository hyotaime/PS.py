import sys

input = sys.stdin.readline
n, b = map(int, input().split())
a, b = map(int, input().split())
rst = 1
while b > 0:
    if b & 1:
        rst = rst * a
    a = a * a
    b >>= 1
print(rst)
