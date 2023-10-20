import sys

input = sys.stdin.readline
y, m, d = map(int, input().split('-'))
if m > 9 or (m == 9 and d > 16):
    print("TOO LATE")
else:
    print("GOOD")
