import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
dir = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
cnt = 0
room = [list(map(int, input().split())) for _ in range(N)]
while True:
    if room[r][c] == 0:
        room[r][c] = -1
        cnt += 1
    if room[r + 1][c] != 0 and room[r - 1][c] != 0 and room[r][c + 1] != 0 and room[r][c - 1] != 0:
        if room[r - dir[d][1]][c - dir[d][0]] == 1:
            break
        else:
            r, c = r - dir[d][1], c - dir[d][0]
    else:
        for _ in range(4):
            d = (d + 3) % 4
            if room[r + dir[d][1]][c + dir[d][0]] == 0:
                r, c = r + dir[d][1], c + dir[d][0]
                break
print(cnt)
