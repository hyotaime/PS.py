import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    w = sum(list(map(int, input().split())))
    if w == 0:
        print('Equilibrium')
    elif w > 0:
        print('Right')
    else:
        print('Left')
