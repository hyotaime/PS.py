import sys

input = sys.stdin.readline
s = input().rstrip()
print(s[0] + s[1:-1] + s[1:-1] + s[-1])
