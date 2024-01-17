import sys

input = sys.stdin.readline
n = int(input())
for _ in range(9):
    n -= int(input())
print(n)
