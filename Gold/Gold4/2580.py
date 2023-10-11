import sys

input = sys.stdin.readline


def chk(arr, row, col, num):
    for i in range(9):
        if arr[row][i] == num or arr[i][col] == num or arr[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True


def dfs(arr):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                for num in range(1, 10):
                    if chk(arr, row, col, num):
                        arr[row][col] = num
                        if dfs(arr):
                            return True
                        arr[row][col] = 0
                return False
    return True


arr = [list(map(int, input().split())) for _ in range(9)]
dfs(arr)
for i in range(9):
    print(*arr[i])
