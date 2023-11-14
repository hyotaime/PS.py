import sys

input = sys.stdin.readline
n = int(input())
order = []
nums = list(map(int, input().split()))
for i in range(n):
    order.insert(i-nums[i], i+1)
print(*order)
