import sys

input = sys.stdin.readline
n, p, s = map(int, input().split())
for _ in range(s):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    if p in arr:
        print("KEEP")
    else:
        print("REMOVE")

