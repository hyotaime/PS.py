i = 1
while True:
    n = int(input())
    if n == 0:
        break
    rst = 0
    cnt = [0, 0, 0]
    for _ in range(n):
        arr = list(map(int, input().split()))
        cnt[0] += arr[0]
        cnt[1] += arr[1]
        cnt[2] += arr[2]
        rst += arr[0] * (0.80 - (15.5 / 85))
        rst += arr[1] * (1.00 - (32 / 85))
        rst += arr[2] * (1.20 - (40 / 85))
        rst += arr[3] * 0.60
    print(f"Case #{i}: RM{rst:.2f}")
    i += 1