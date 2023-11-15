import sys

input = sys.stdin.readline
n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    d[a] = b
m = int(input())
for _ in range(m):
    c = input().rstrip()
    if c in d:
        print(d[c], end="")
    else:
        print(c, end="")
