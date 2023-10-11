import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    i, w = map(int, input().split())
    print("Yes" if (i <= 1 and w <= 2) or (i <= 2 and w <= 1) else "No")
