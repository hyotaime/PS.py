import sys

input = sys.stdin.readline
n = int(input())
rst, tmp = 0, 0
for i in range(n):
    t = int(input())
    if i % 2 == 0:
        tmp = t
    else:
        rst += t - tmp
if n % 2 == 1:
    print("still running")
else:
    print(rst)
