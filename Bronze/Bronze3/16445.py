import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
for _ in range(n):
    g = int(input())
    if g != 1:
        cnt += 1
print(cnt)
