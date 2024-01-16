import sys

input = sys.stdin.readline
n = int(input())
dp = [i for i in range(n + 1)]
for i in range(1, int(n ** 0.5) + 1):
    dp[i ** 2] = 1
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
print(dp[n])
