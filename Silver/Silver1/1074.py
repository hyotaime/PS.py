import sys

input = sys.stdin.readline
N, r, c, = map(int, input().split())
cnt = 0
while N > 0:
    N -= 1
    if r < 2 ** N and c < 2 ** N:
        cnt += 2 ** (2 * N) * 0
        r -= 0
        c -= 0
    elif r < 2 ** N <= c:
        cnt += 2 ** (2 * N) * 1
        r -= 0
        c -= 2 ** N
    elif r >= 2 ** N > c:
        cnt += 2 ** (2 * N) * 2
        r -= 2 ** N
        c -= 0
    else:
        cnt += 2 ** (2 * N) * 3
        r -= 2 ** N
        c -= 2 ** N
print(cnt)
