import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = {}

i = 0
tmp = 1
for x in sorted(a):
    if x not in d:
        i += tmp
        tmp = 1
        d[x] = i
    else:
        d[x] = i
        tmp += 1

for x in a:
    print(d[x])
