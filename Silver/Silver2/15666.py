import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

tmp = []
rst = set()


def sol(x):
    if len(tmp) == m:
        rst.add(tuple(tmp))
        return
    for i in range(x, n):
        tmp.append(arr[i])
        sol(i)
        tmp.pop()


sol(0)

for i in sorted(rst):
    print(*i)
