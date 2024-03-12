import sys

input = sys.stdin.readline
s = input().strip()
cnt = 0
for c in s:
    if c in 'aeiou':
        cnt += 1
print(cnt)
