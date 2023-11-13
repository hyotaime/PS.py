import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
for i in range(1, n):
    if s[i] == "J":
        print(s[i-1])
