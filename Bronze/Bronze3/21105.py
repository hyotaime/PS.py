import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    p, c = map(float, input().split())
    print(100 * p / (c + 100))
