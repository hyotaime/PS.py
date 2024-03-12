import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    if sum(arr) == 180:
        print(*arr, "Seems OK")
    else:
        print(*arr, "Check")
