import sys

input = sys.stdin.readline
m = int(input())
rst = 0
if m <= 30:
    rst = m * 0.5
else:
    rst = 15 + (m - 30) * 1.5
print(rst)
