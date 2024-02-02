import sys

input = sys.stdin.readline
n = int(input())
rst = 0
x, y = map(int, input().split())
for _ in range(n - 1):
    a, b = map(int, input().split())
    rst += abs(x - a) + abs(y - b)
    x, y = a, b

print(rst)
