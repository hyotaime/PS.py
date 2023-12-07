import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    for n in str(i):
        if n == str(c):
            cnt += 1
print(cnt)
