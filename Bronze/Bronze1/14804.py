t = int(input())
for i in range(t):
    d, n = map(int, input().split())
    rst = float('inf')
    for _ in range(n):
        k, s = map(int ,input().split())
        rst = min(rst, (d / ((d - k) / s)))
    print(f"Case #{i + 1}: {rst}")