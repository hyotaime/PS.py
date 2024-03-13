import sys

input = sys.stdin.readline
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
h, m, s = map(int, input().split())
cnt = h * b1 * c1 + m * c1 + s
r1, r2, r3 = 0, 0, 0
if b2 == 1 and c2 == 1:
    r3 = cnt
elif b2 == 1:
    r1 = cnt // c2 % a2
    r3 = cnt % c2
elif c2 == 1:
    r1 = cnt // b2 % a2
    r2 = cnt % b2
else:
    r1 = cnt // b2 // c2 % a2
    r2 = cnt // c2 % b2
    r3 = cnt % c2
print(r1, r2, r3)
