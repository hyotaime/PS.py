import sys

input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(dp[i])):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) if j != 0 and j != len(dp[i])-1 else dp[i-1][j-1] if j == len(dp[i])-1 else dp[i-1][j]
print(max(dp[n-1]))
