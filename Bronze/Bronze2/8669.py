import sys

input = sys.stdin.readline
n = int(input())
cnt = [False] * 1000000
for _ in range(n):
    g, r = map(int, input().split())
    cnt[r-1] = True
rst = 0
for i in range(1000000):
    if cnt[i]:
        rst += 1
print(rst)
