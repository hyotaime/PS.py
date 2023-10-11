import sys

input = sys.stdin.readline
r, c, n = map(int, input().split())
print((r // n + (1 if r % n else 0)) * (c // n + (1 if c % n else 0)))
