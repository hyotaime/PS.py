import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    c = input().strip()
    print(len(c))
