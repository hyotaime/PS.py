from collections import deque

t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1, arr2 = [], []
    for i in arr:
        if i % 2 == 0:
            arr2.append(i)
        else:
            arr1.append(i)
    arr1.sort()
    arr1 = deque(arr1)
    arr2.sort(reverse=True)
    arr2 = deque(arr2)
    rst = []
    for i in arr:
        if i % 2 == 0:
            rst.append(str(arr2.popleft()))
        else:
            rst.append(str(arr1.popleft()))

    print(f"Case #{j + 1}: {' '.join(rst)}")