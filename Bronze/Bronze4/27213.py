import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
if n == 1 or m == 1:
    print(max(n, m))
else:
    print(2*(n + m) - 4)
