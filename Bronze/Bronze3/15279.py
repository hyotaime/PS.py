import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    b, p = map(float, input().split())
    print(f'{60 * (b - 1) / p:.4f} {60 * b / p:.4f} {60 * (b + 1) / p:.4f}')
