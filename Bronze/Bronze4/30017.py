import sys

input = sys.stdin.readline
a, b = map(int, input().split())
if a > b:
    print(2 * b + 1)
elif a <= b:
    print(2 * a - 1)
