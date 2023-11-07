import sys

input = sys.stdin.readline
# 재귀 한도 설정
sys.setrecursionlimit(10 ** 6)


def sol(left, right, p):
    # 재귀 종료 조건
    if left == 1 and right == n:
        return 0
    if dp[left][right][p] != float('inf'):
        return dp[left][right][p]
    dp[left][right][p] = float('inf')
    # 왼쪽으로 이동하는 경우
    if left > 1:
        dp[left][right][p] = sol(left - 1, right, 0) + (sum - (prefix_sum[right] - prefix_sum[left - 1])) * (
                (rooms[right][0] if p else rooms[left][0]) - rooms[left - 1][0])
    # 오른쪽으로 이동하는 경우
    if right < n:
        dp[left][right][p] = min(dp[left][right][p],
                                 sol(left, right + 1, 1) + (sum - (prefix_sum[right] - prefix_sum[left - 1])) * (
                                         rooms[right + 1][0] - (rooms[right][0] if p else rooms[left][0])))
    return dp[left][right][p]


# 입력
n, m = map(int, input().split())
rooms = [(0, 0)]
for _ in range(n):
    d, w = map(int, input().split())
    rooms.append((d, w))

# 3차원 DP[left][right][p]
dp = [[[float('inf') for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]

# 전력 소모 prefix sum
prefix_sum = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + rooms[i][1]
sum = prefix_sum[n]

# 출력
print(sol(m, m, 0))
