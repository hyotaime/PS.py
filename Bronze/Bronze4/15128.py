import sys

input = sys.stdin.readline
p1, q1, p2, q2 = map(int, input().split())
rst = p1*p2/q1/q2/2
if rst == int(rst):
    print(1)
else:
    print(0)
