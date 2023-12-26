import sys

input = sys.stdin.readline
N = int(input())
seat = [[0] * N for _ in range(N)]
suki = {}
rst = 0


def blank_chk():
    for i in range(N):
        for j in range(N):
            if i > 0:
                if seat[i - 1][j] == 0:
                    blank[i][j] += 1
            if j > 0:
                if seat[i][j - 1] == 0:
                    blank[i][j] += 1
            if i < N - 1:
                if seat[i + 1][j] == 0:
                    blank[i][j] += 1
            if j < N - 1:
                if seat[i][j + 1] == 0:
                    blank[i][j] += 1


def suki_chk(num):
    for i in range(N):
        for j in range(N):
            if seat[i][j] in suki[num]:
                if i > 0:
                    if seat[i - 1][j] == 0:
                        suki_domo[i - 1][j] += 1
                if j > 0:
                    if seat[i][j - 1] == 0:
                        suki_domo[i][j - 1] += 1
                if i < N - 1:
                    if seat[i + 1][j] == 0:
                        suki_domo[i + 1][j] += 1
                if j < N - 1:
                    if seat[i][j + 1] == 0:
                        suki_domo[i][j + 1] += 1


for _ in range(N ** 2):
    blank = [[0] * N for _ in range(N)]
    blank_chk()
    tmp = list(map(int, input().split()))
    num = tmp[0]
    suki[num] = tmp[1:]
    suki_domo = [[0] * N for _ in range(N)]
    suki_chk(num)
    max_suki = 0
    max_suki_list = []
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                if suki_domo[i][j] > max_suki:
                    max_suki = suki_domo[i][j]
                    max_suki_list = [(i, j)]
                elif suki_domo[i][j] == max_suki:
                    max_suki_list.append((i, j))
    if len(max_suki_list) == 1:
        seat[max_suki_list[0][0]][max_suki_list[0][1]] = num
    else:
        max_blank = 0
        max_blank_list = []
        for i, j in max_suki_list:
            if blank[i][j] > max_blank:
                max_blank = blank[i][j]
                max_blank_list = [(i, j)]
            elif blank[i][j] == max_blank:
                max_blank_list.append((i, j))
        seat[max_blank_list[0][0]][max_blank_list[0][1]] = num

for i in range(N):
    for j in range(N):
        cnt = 0
        if i > 0:
            if seat[i - 1][j] in suki[seat[i][j]]:
                cnt += 1
        if j > 0:
            if seat[i][j - 1] in suki[seat[i][j]]:
                cnt += 1
        if i < N - 1:
            if seat[i + 1][j] in suki[seat[i][j]]:
                cnt += 1
        if j < N - 1:
            if seat[i][j + 1] in suki[seat[i][j]]:
                cnt += 1
        if cnt == 0:
            rst += 0
        else:
            rst += 10 ** (cnt - 1)


print(rst)
