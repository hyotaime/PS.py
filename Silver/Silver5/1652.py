import sys

input = sys.stdin.readline
n = int(input())
room = [input().rstrip() for _ in range(n)]
cnt_h, cnt_v = 0, 0
for i in range(n):
    space = room[i].split('X')
    for s in space:
        if len(s) >= 2:
            cnt_h += 1
for i in range(n):
    space = ""
    for j in range(n):
        space += room[j][i]
    space = space.split('X')
    for s in space:
        if len(s) >= 2:
            cnt_v += 1
print(cnt_h, cnt_v)
