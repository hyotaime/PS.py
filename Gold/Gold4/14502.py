import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rst = 0
empty = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))

block = list(combinations(empty, 3))

virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))

for b in block:
    tmp = copy.deepcopy(lab)
    for y, x in b:
        tmp[y][x] = 1

    queue = deque(virus)
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                queue.append((ny, nx))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    rst = max(rst, cnt)
print(rst)
