import sys

input = sys.stdin.readline
x = int(input())
n = int(input())
rst = 0
for _ in range(n):
    p = int(input())
    rst = rst + x - p
print(rst + x)
