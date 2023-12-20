import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = {}
for i in arr:
    if i in d:
        d[i] = False
    else:
        d[i] = True
for i in arr:
    if d[i]:
        print(i)
        break
