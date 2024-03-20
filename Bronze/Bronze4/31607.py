import sys

input = sys.stdin.readline
arr = [int(input()), int(input()), int(input())]
arr.sort()
print(1 if arr[0] + arr[1] == arr[2] else 0)
