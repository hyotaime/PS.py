import sys

input = sys.stdin.readline
n = int(input())
S_x = 0
S_y = 0
S_xx = 0
S_xy = 0

for _ in range(n):
    x, y = map(int, input().split())
    S_x += x
    S_y += y
    S_xx += pow(x, 2)
    S_xy += x * y

if S_x * S_x != n * S_xx:
    a_2 = (n * S_xy - S_x * S_y) / (n * S_xx - pow(S_x, 2))
    b_2 = (S_y - a_2 * S_x) / n
    print(f"{a_2:.10f} {b_2:.10f}")
else:
    print("EZPZ")
