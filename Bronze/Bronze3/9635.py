import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    if arr[0] == x and arr[-1] == y:
        print('BOTH')
    elif arr[0] == x:
        print('EASY')
    elif arr[-1] == y:
        print('HARD')
    else:
        print('OKAY')
