import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [True] * n
cnt = n
num = list(map(int, input().split()))
for i in num:
    arr[i - 1] = False
    cnt -= 1
num = list(map(int, input().split()))
for i in num:
    arr[i - 1] = False
    cnt -= 1
print(cnt)
for i in range(n):
    if arr[i]:
        print(i + 1, end=' ')
