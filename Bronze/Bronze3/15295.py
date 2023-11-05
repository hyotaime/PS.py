import sys

input = sys.stdin.readline
p = int(input())
for _ in range(p):
    k, n = map(int, input().split())
    print(k, int((n + 1) * n / 2 + n))
