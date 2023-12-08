import sys

input = sys.stdin.readline
t = int(input())
d = {}
for _ in range(t):
    a, b = map(str, input().split())
    d[b] = a
s = input().rstrip()
for i in range(0, len(s), 4):
    if s[i:i+4] in d:
        print(d[s[i:i+4]], end='')
    else:
        print('?', end='')
