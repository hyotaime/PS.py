import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    rst = (10000, 0)
    for i in range(n):
        if abs(arr[i]-2023) < rst[0]:
            rst = (abs(arr[i]-2023), i+1)
    print(rst[1])
