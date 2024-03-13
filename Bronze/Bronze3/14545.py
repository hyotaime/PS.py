import sys

input = sys.stdin.readline
p = int(input())
for _ in range(p):
    l = int(input())
    rst = 0
    for i in range(1, l + 1):
        rst += i ** 2
    print(rst)
