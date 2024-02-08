import sys

input = sys.stdin.readline
n = int(input())
rst = 0
b = int(input())
for _ in range(n - 1):
    p = int(input())
    if b < p:
        rst += p - b
    if b > p:
        b = p
print(rst)
