import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
rst = 0
for i in range(n):
    rst += arr[i]//m
print(rst)
