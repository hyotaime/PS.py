import sys

input = sys.stdin.readline
n = int(input())
bd = set()
for _ in range(n):
    s = input().rstrip()
    bd.add(s)

print(len(bd))
