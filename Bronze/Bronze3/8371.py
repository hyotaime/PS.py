import sys

input = sys.stdin.readline
n = int(input())
a = input().rstrip()
b = input().rstrip()
cnt = 0
for i in range(n):
    if a[i] != b[i]:
        cnt += 1
print(cnt)
