import sys

input = sys.stdin.readline
S, N, M = map(int, input().split())
len = S
U = 0
for _ in range(N+M):
    d = int(input())
    match d:
        case 0:
            U -= 1
            if U <= len//2:
                len //= 2
        case 1:
            U += 1
            if U > len:
                len *= 2
print(len)
