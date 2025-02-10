n = int(input())
k = int(input())
arr = set()
rst = 0
for _ in range(k):
    i = int(input())
    for j in range(i, n + 1, i):
        if j in arr:
            arr.remove(j)
        else:
            arr.add(j)
    rst = max(rst, len(arr))

print(rst)