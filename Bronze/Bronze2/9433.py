n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    flag = True
    while flag:
        flag = False
        for i in range(1, len(arr)):
            if arr[i] > 1:
                flag = True
        for i in range(1, len(arr)):
            arr[i - 1] += arr[i] // 2
            if arr[i] % 2 == 0:
                arr[i] = 0
            else:
                arr[i] = 1
    print(*arr)