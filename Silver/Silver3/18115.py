import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
rst = deque()
for i in range(n):
    if arr[i] == 1:
        rst.appendleft(i + 1)
    elif arr[i] == 2:
        rst.insert(1, i + 1)
    else:
        rst.append(i + 1)
print(*rst)
