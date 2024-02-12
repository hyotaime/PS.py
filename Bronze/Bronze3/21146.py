import sys

input = sys.stdin.readline
n, k = map(int, input().split())
rst = 0
for _ in range(k):
    r = int(input())
    rst += r

print((rst - (n - k) * 3) / n, (rst + (n - k) * 3) / n)
