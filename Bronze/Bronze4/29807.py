import sys

input = sys.stdin.readline
t = int(input())
rst = 0
sc = [0, 0, 0, 0, 0]
s = list(map(int, input().split()))
for i in range(t):
    sc[i] = s[i]
rst += (sc[0] - sc[2]) * 508 if sc[0] > sc[2] else (sc[2] - sc[0]) * 108
rst += (sc[1] - sc[3]) * 212 if sc[1] > sc[3] else (sc[3] - sc[1]) * 305
rst += sc[4] * 707 if t == 5 else 0
print(rst * 4763)
