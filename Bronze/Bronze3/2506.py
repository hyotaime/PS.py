n = int(input())
arr = list(map(int, input().split()))
rst = 0
cnt = 0
for i in arr:
    if i == 0:
        cnt = 0
    else:
        cnt += 1
        rst += cnt
print(rst)
