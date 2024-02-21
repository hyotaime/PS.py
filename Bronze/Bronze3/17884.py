import sys

input = sys.stdin.readline
n = int(input())
d = list(map(int, input().split()))
rst = [0] * n
rst[0] = 1
for i in range(n - 1):
    rst[d[i] + 1] = i + 2
print(*rst)
