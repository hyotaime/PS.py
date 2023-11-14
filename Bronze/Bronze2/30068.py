import sys

input = sys.stdin.readline
m = int(input())
parking = {}
for _ in range(m):
    t, n = map(int, input().split())
    if n in parking:
        print(n, t - parking[n])
    else:
        parking[n] = t
