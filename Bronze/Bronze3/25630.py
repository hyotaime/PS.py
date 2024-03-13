import sys

input = sys.stdin.readline
n = int(input())
s = input().strip()
cnt = 0
for i in range(n // 2):
    if s[i] != s[::-1][i]:
        cnt += 1
print(cnt)
