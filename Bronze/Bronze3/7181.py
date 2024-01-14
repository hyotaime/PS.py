import sys

input = sys.stdin.readline
s = input().rstrip()
n = int(input())
for _ in range(n):
    a, b = 0, 0
    q = input().rstrip()
    for i in range(4):
        if q[i] in s:
            a += 1
        if q[i] == s[i]:
            b += 1
    print(a, b)
