n = int(input())
rst, cnt = 0, 0
while n:
    rst += 1
    cnt += 1
    if cnt > n:
        cnt = 1

    n -= cnt

print(rst)
