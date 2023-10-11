import sys

input = sys.stdin.readline
N, B = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]


def mul(a, b):
    return [[sum([a[i][k] * b[k][j] for k in range(N)]) % 1000 for j in range(N)] for i in range(N)]


def div(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    elif b % 2:
        return mul(div(a, b - 1), a)
    else:
        return div(mul(a, a), b // 2)


for i in div(matrix, B):
    print(*i)
