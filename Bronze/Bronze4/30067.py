import sys

input = sys.stdin.readline
n = [int(input()) for _ in range(10)]
for i in range(10):
    if sum(n) == 2*n[i]:
        print(n[i])
        break
