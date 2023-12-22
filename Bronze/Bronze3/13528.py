import sys

input = sys.stdin.readline
c = float(input())
l = int(input())
rst = 0
for _ in range(l):
    width, length = map(float, input().split())
    rst += width * length * c
print(rst)
