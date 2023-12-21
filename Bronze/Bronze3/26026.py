import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
coffee = 0
cnt = 0
for i in s:
    if i == '1':
        cnt += 1
        coffee = 2
    elif i == '0' and coffee != 0:
        cnt += 1
        coffee -= 1
print(cnt)
