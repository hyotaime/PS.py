import sys

input = sys.stdin.readline
n = int(input())
rst = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        rst = min(rst, b)
if rst == 1001:
    print(-1)
else:
    print(rst)
