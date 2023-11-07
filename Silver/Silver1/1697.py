import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()
q.append(n)
arr = [0] * 100001
while q:
    d = q.popleft()
    if d == k:
        print(arr[d])
        break
    for i in (d - 1, d + 1, d * 2):
        if 0 <= i <= 100000 and not arr[i]:
            arr[i] = arr[d] + 1
            q.append(i)
