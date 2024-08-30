n, l, k = map(int, input().split())
rst = 0
arr = [int(input()) for _ in range(n)]
arr.sort()
for r in arr:
    if r <= l:
        rst += 1
        l += k

print(rst)
