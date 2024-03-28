m = int(input())
arr = [1, 2, 3]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]
for i in range(3):
    if arr[i] == 1:
        print(i + 1)