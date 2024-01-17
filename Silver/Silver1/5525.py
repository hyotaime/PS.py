import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()
cnt, rst = 0, 0
idx = 0
while idx < m - 2:
    if s[idx:idx + 3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == n:
            rst += 1
            cnt -= 1
    else:
        cnt = 0
        idx += 1
print(rst)
