t = int(input())
arr = [0] * 302
for i in range(1, 302):
    arr[i] = arr[i - 1] + i

for _ in range(t):
    n = int(input())
    rst = 0
    for i in range(1, n + 1):
        rst += i * arr[i + 1]
    print(rst)
