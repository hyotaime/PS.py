import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(str, input().split()))
cnt = 0
for a in arr:
    if a == 'he' or a == 'she' or a == 'him' or a == 'her':
        cnt += 1
print(cnt)
