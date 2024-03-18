import sys

input = sys.stdin.readline
k = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
cnt = 0
for i in arr1:
    for j in arr2:
        if i + k == j:
            cnt += 1
print(cnt)
