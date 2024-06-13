import math

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
rst = 1
for i in range((n + 1) // 2):
    rst += int(math.log2(arr[i]))

print(rst)
