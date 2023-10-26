import sys

input = sys.stdin.readline
n = int(input())
rst = 0
for _ in range(n):
    q, y = map(float, input().split())
    rst += q * y
print(f"{rst:.3f}")
