import sys

input = sys.stdin.readline
y, m = map(int, input().split())
a, b = 0, 0
if y == 0:
    b += int(12 * (15 * (m / 12) - int(15 * (m / 12))) + 0.5)
    a += int(15 * (m / 12))
if y == 1:
    b += int(12 * (9 * (m / 12) - int(9 * (m / 12))) + 0.5)
    a += 15 + int(9 * (m / 12))
if y >= 2:
    b += int(12 * (4 * (m / 12) - int(4 * (m / 12))) + 0.5)
    a += int(4 * (m / 12)) + (y - 2) * 4 + 15 + 9

print(a, b)
