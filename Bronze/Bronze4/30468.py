import sys

input = sys.stdin.readline
s, d, i, l, n = map(int, input().split())
sum = s + d + i + l
n *= 4
rst = 0
if sum < n:
    rst += n - sum
print(rst)
