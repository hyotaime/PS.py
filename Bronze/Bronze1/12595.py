import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if nums.count(num) == 1:
            print(f"Case #{i+1}: {num}")
            break
