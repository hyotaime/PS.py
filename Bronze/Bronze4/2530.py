import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
d = int(input())
c += d % 60
b += d // 60 % 60
a += d // 3600
if c >= 60:
    b += c // 60
    c %= 60
if b >= 60:
    a += b // 60
    b %= 60
if a >= 24:
    a %= 24
print(a, b, c)
