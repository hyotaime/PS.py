import sys

input = sys.stdin.readline


def com(irt, l):
    if l == m:
        print(*rst)
        return
    for i in range(irt, n):
        rst[l] = arr[i]
        com(i, l + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    rst = [0] * m
    com(0, 0)
