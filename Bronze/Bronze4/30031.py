import sys

input = sys.stdin.readline
n = int(input())
rst = 0
for _ in range(n):
    w, h = map(int, input().split())
    match w:
        case 154:
            rst += 50000
        case 148:
            rst += 10000
        case 142:
            rst += 5000
        case 136:
            rst += 1000
print(rst)
