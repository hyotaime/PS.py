import sys

input = sys.stdin.readline
n = int(input())
d = {}
for i in range(1, n + 1):
    k = int(input())
    d[k] = i
for i in range(1, n + 1):
    print(d[i])
