import sys

input = sys.stdin.readline
n = int(input())
rst = float('inf')
for _ in range(n):
    a, b = map(int, input().split())
    rst = min(rst, b // a)
print(rst)
