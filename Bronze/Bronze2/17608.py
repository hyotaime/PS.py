import sys

input = sys.stdin.readline
n = int(input())
sticks = []
for _ in range(n):
    sticks.append(int(input()))
sticks.reverse()
cnt = 1
stick_max = sticks[0]
for i in range(1, n):
    if sticks[i] > stick_max:
        stick_max = sticks[i]
        cnt += 1
print(cnt)
