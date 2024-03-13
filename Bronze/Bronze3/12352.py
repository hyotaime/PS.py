import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for j in range(1, n - 1):
        if arr[j] > (arr[j - 1] + arr[j + 1]) / 2:
            arr[j] = (arr[j - 1] + arr[j + 1]) / 2
    print(f'Case #{i + 1}: {arr[n - 2]:.6f}')
