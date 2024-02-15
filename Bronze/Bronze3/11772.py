import sys

input = sys.stdin.readline
n = int(input())
rst = 0
for _ in range(n):
    s = input().rstrip()
    num, p = int(s[:-1]), int(s[-1])
    rst += pow(num, p)
print(rst)
