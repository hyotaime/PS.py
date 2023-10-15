import sys

input = sys.stdin.readline
n = int(input())
dp = [[0] * 3 for _ in range(n+1)]
cost = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i - 1][2]
print(min(dp[n][0], dp[n][1], dp[n][2]))
