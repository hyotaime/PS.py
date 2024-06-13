n = int(input())
rst = 0
for i in range(n + 1):
    for j in range(i + 1):
        rst += i + j
print(rst)
