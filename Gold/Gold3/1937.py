import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]


def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = 1
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if graph[nr][nc] > graph[r][c]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]


rst = 0
for i in range(n):
    for j in range(n):
        rst = max(rst, dfs(i, j))
print(rst)
