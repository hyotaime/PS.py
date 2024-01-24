import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
broken = []
if m != 0:
    broken = list(map(int, input().split()))
rst = abs(n - 100)

for i in range(1000001):
    chk = True
    for j in str(i):
        if int(j) in broken:
            chk = False
            break
    if chk:
        rst = min(rst, len(str(i)) + abs(i - n))

print(rst)
