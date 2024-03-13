import sys

input = sys.stdin.readline
n = int(input())
a = input().strip()
b = input().strip()
cnt = 0
for i in range(n):
    cnt += min(abs(ord(a[i]) - ord(b[i])), 26 - abs(ord(a[i]) - ord(b[i])))
print(cnt)
