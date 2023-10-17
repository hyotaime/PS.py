import sys

input = sys.stdin.readline
a, b = map(int, input().split())
print("E" if a >= b/2 else "H")
