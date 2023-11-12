import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(2 * x - y, y - x)
