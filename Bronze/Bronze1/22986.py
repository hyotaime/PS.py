t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n < k:
        k = n
    rst = 2 * (k + 1) * (2 * n - k)
    print(rst)
