n = int(input())
arr = list(map(str, input().split()))
for s in arr:
    if s[0] != arr[0][0]:
        print(0)
        exit()
print(1)
