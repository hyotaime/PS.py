import sys

input = sys.stdin.readline
n = int(input())
s = {}
for _ in range(n):
    a, b = input().split()
    if a not in s:
        s[a] = int(b)
    else:
        s[a] += int(b)
for i in sorted(s):
    print(i, s[i])
