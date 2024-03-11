import sys

input = sys.stdin.readline
a, b = map(int, input().split())
print(((b + a) * a + a) * a)
