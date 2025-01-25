while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    rst = [1] * n
    for _ in range(d):
        arr = list(map(int, input().split()))
        for i in range(n):
            rst[i] *= arr[i]
    if rst.count(1):
        print("yes")
    else:
        print("no")
