import sys

input = sys.stdin.readline
w, n, p = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    if w <= a <= n:
        cnt += 1
print(cnt)
