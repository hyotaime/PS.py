import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
rst = b - a
print(rst if rst > 0 else rst+24)
