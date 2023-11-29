import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s[-1] != '.':
        s += '.'
    print(s)
