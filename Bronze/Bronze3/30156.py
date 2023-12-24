import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().rstrip()
    cnt1, cnt2 = 0, 0
    for c in s:
        if c == 'a':
            cnt1 += 1
        else:
            cnt2 += 1
    print(min(cnt1, cnt2))
