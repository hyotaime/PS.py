import sys

input = sys.stdin.readline
n = int(input())
s = str(input().strip())
h, v = 0, 0
for _ in s:
    match _:
        case 'N':
            v += 1
        case 'S':
            v -= 1
        case 'E':
            h += 1
        case 'W':
            h -= 1

print(abs(h)+abs(v))
