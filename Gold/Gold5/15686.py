from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
rst = float('inf')
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
            graph[i][j] = 0

comb = list(combinations(chicken, m))

for chk in comb:
    temp = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                temp += min([abs(i - x) + abs(j - y) for x, y in chk])
    rst = min(rst, temp)
print(rst)
