import sys

input = sys.stdin.readline


def tromino(board, size, x, y, row, col):
    # 가운데 좌표 구함
    mid_x = x + size // 2
    mid_y = y + size // 2

    # 새로운 리스트 생성
    new_row = [mid_x, mid_x - 1, mid_x - 1, mid_x]
    new_col = [mid_y - 1, mid_y - 1, mid_y, mid_y]
    # 4등분
    if row >= mid_x and col < mid_y:
        new_row[0], new_col[0] = row, col
    elif row < mid_x and col < mid_y:
        new_row[1], new_col[1] = row, col
    elif row < mid_x and col >= mid_y:
        new_row[2], new_col[2] = row, col
    else:
        new_row[3], new_col[3] = row, col
    # 재귀함수로 4등분하여 계산
    # 시계방향으로
    if size > 2:
        tromino(board, size // 2, x, y, new_row[1], new_col[1])
        tromino(board, size // 2, mid_x, y, new_row[0], new_col[0])

    for i in range(4):
        if new_row[i] == row and new_col[i] == col:
            continue
        board[new_col[i]][new_row[i]] = globals()['num']

    globals()['num'] += 1

    if size > 2:
        tromino(board, size // 2, x, mid_y, new_row[2], new_col[2])
        tromino(board, size // 2, mid_x, mid_y, new_row[3], new_col[3])


if __name__ == "__main__":
    # 입력
    n = int(input())
    x, y = map(int, input().split())
    size = 2 ** n
    x -= 1
    y -= 1
    board = [[0] * size for _ in range(size)]

    # 빈 칸은 -1로 표시
    board[y][x] = -1
    globals()['num'] = 1

    # tromino
    tromino(board, size, 0, 0, x, y)

    # 출력
    for i in range(size):
        for j in range(size):
            print(board[size - i - 1][j], end=" ")
        print()
