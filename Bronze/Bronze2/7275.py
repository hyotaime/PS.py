import sys

input = sys.stdin.readline
n, k, m = map(int, input().split())
g = []
cnt = 0
for _ in range(k):
    s = list(map(int, input().split()))
    s.remove(s[0])
    g.append(s)

colors = list(map(int, input().split()))
for s in g:
    tmp = 0
    for i in s:
        if colors[i-1] != 0:
            tmp += colors[i-1]
    cnt += (tmp - 1) // m + 1
print(cnt)
