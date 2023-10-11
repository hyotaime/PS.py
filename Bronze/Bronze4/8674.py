import sys

input = sys.stdin.readline
a, b = map(int, input().split())
if a % 2 == 0 or b % 2 == 0:
    print("0")
else:
    print(a if a < b else b)
