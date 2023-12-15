import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
cnt = 0
for n in arr[1:]:
    if arr[0] - n <= 1000:
        cnt += 1
print(cnt)
