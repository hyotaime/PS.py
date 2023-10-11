import sys

input = sys.stdin.readline
d, h, m = map(int, input().split())
rst = (d-11)*60*24 + (h-11)*60 + (m-11)
print(rst if rst >= 0 else -1)
