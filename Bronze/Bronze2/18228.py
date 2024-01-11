import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
rst = 0
tmp = float('inf')
for i in arr:
    if i == -1:
        rst += tmp
        tmp = float('inf')
    else:
        tmp = min(tmp, i)
print(rst + tmp)
