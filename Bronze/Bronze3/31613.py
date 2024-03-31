import sys

input = sys.stdin.readline
x = int(input())
n = int(input())
cnt = 0
while x < n:
    cnt += 1
    match x % 3:
        case 0:
            x += 1
        case 1:
            x *= 2
        case 2:
            x *= 3
print(cnt)
