import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
if sum(arr) == 0:
    print('Stay')
else:
    print("Right" if sum(arr) > 0 else "Left")
