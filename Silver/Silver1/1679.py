# BFS MLE
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
nums = set(arr)
dp = [float('inf') for _ in range(arr[-1] * k + 2)]

for i in range(1, arr[-1] * k + 2):
    if i in nums:
        dp[i] = 1
    else:
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
    if dp[i] > k:
        if i % 2 == 0:
            print("holsoon win at", i)
        else:
            print("jjaksoon win at", i)
        break
