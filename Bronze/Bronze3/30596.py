import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(4)]
arr.sort()
print(arr[0] * arr[2])
