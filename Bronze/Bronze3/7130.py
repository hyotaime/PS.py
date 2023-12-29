import sys

input = sys.stdin.readline
m, h = map(int, input().split())
n = int(input())
rst = 0
for _ in range(n):
    c, b = map(int, input().split())
    rst += max(c * m, b * h)
print(rst)
