import sys

input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    pw = input().rstrip()
    s.add(pw)
    if pw[::-1] in s:
        print(len(pw), pw[len(pw)//2])
        break
