import sys

input = sys.stdin.readline
c = input().rstrip()
rst = 0
pw = 'ILOVEYONSEI'
for n in pw:
    rst += abs(ord(c) - ord(n))
    c = n
print(rst)
