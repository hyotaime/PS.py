r, c = map(int, input().split())
arr = [list(map(str, input())) for _ in range(r)]
rst = [0, 0, 0, 0, 0]
for i in range(r - 1):
    for j in range(c - 1):
        cnt = 0
        if arr[i][j] == '#' or arr[i + 1][j] == '#' or arr[i][j + 1] == '#' or arr[i + 1][j + 1] == '#':
            continue
        for x in range(2):
            for y in range(2):
                if arr[i + x][j + y] == 'X':
                    cnt += 1
        rst[cnt] += 1
for i in rst:
    print(i)
