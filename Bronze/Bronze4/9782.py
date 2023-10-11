import sys

input = sys.stdin.readline
cnt = 1
while True:
    arr = list(map(float, input().split()))
    n = int(arr[0])
    if n == 0:
        break
    if n % 2 == 0:
        rst = (arr[n//2] + arr[(n//2)+1]) / 2
    else:
        rst = arr[(n+1)//2]
    print(f"Case {cnt}: {rst}")
    cnt += 1
