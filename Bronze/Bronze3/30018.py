import sys

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
rst = 0
for i in range(n):
    rst += abs(arr1[i] - arr2[i])
print(rst // 2)
