arr = []
for _ in range(5):
    arr.append(sum(map(int, input().split())))
for i in range(5):
    if arr[i] == max(arr):
        print(i + 1, max(arr))
        break
