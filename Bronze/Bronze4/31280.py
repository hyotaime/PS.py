import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
arr.sort()
print(sum(arr) - arr[0] + 1)
