import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
cnt0, cnt1 = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            cnt1 += 1
        else:
            cnt0 += 1
print(min(cnt0, cnt1))
