n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                continue
            x, y, z = arr[i], arr[j], arr[k]
            if x == y:
                continue
            if (x - y) % z == 0:
                continue
            print("no")
            exit()
print("yes")
