import sys

input = sys.stdin.readline
n, h = map(int, input().split())
list = list(map(int, input().split()))
cnt = 0
for i in list:
    if h >= i:
        cnt += 1
print(cnt)
