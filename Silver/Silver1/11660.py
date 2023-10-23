import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (n+1) for _ in range(n+1)]

# 2차원 누적합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

# 전체 합에서 범위에 포함되지 않는 부분을 빼준다.
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])
