import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr = arr + arr[:1]

rst = 0
for i in range(n):
    rst += abs(arr[i][0] - arr[i + 1][0]) + abs(arr[i][1] - arr[i + 1][1])

print(rst)
