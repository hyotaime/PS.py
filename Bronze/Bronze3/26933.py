import sys

input = sys.stdin.readline
n = int(input())
rst = 0
for _ in range(n):
    h, b, k = map(int, input().split())
    if h < b:
        rst += (b - h) * k
print(rst)
