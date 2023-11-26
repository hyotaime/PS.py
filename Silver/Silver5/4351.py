import sys

input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
    h, p = input().split()
    d[h] = int(p)
for _ in range(m):
    cnt = 0
    while True:
        s = input().rstrip()
        if s == '.':
            break
        for word in s.split():
            if word in d:
                cnt += d[word]
    print(cnt)
