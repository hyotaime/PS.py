import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cancel = 0
    n, m = map(int, input().split())
    bottom = list(map(int, input().split()))
    left = list(map(int, input().split()))
    for i in bottom:
        if i in left:
            cancel += 1
    print(cancel)
