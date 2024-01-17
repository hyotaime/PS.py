import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    for i in range(x, m * n + 1, m):
        if i % n == y % n:
            print(i)
            break
    else:
        print(-1)
