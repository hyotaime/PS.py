n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())
match k:
    case 1:
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end='')
            print()
    case 2:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                print(arr[i][j], end='')
            print()
    case 3:
        for i in range(n - 1, -1, -1):
            for j in range(n):
                print(arr[i][j], end='')
            print()

