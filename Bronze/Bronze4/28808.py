import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
for _ in range(n):
    s = input()
    if '+' in s:
        cnt += 1

print(cnt)
