import sys

input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
cnt = 0
for i in range(n):
    c = input().rstrip()
    if c == arr[i]:
        cnt += 1
print(cnt)
