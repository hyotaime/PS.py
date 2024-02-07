import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
rst = 0
for i in range(k + 1):
    rst += n * (10 ** i)
print(rst)
