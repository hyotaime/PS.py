import sys

input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    s.add(input().rstrip())
print(n - len(s))
