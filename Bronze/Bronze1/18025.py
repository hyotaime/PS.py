n = int(input())
arr = list(map(int, input().split()))
rst = (0, float('inf'))
for i in range(n - 2):
    if max(arr[i], arr[i + 2]) < rst[1]:
        rst = (i + 1, max(arr[i], arr[i + 2]))
print(*rst)
