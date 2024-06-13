n = int(input())
arr1, arr2 = [], []
for _ in range(n):
    s = input()
    for i in range(1, len(s) // 2 + 1):
        if s[:i] * (len(s) // i) == s:
            arr1.append(i)
            break
    else:
        arr1.append(len(s))

for _ in range(n):
    s = input()
    for i in range(1, len(s) // 2 + 1):
        if s[:i] * (len(s) // i) == s:
            arr2.append(i)
            break
    else:
        arr2.append(len(s))

arr1.sort()
arr2.sort()
rst = 0
for i in range(n):
    rst += (arr1[i] - arr2[i]) ** 2

print(rst)
