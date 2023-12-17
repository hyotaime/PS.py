import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1, y1, f1, x2, y2, f2 = map(int, input().split())
    print(f1 + abs(x1 - x2) + abs(y1 - y2) + f2)
