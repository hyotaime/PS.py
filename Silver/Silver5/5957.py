n = int(input())
arr1, arr2, arr3 = [n - i for i in range(n)], [], []
while arr1 or arr2:
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b):
            arr2.append(arr1.pop())
    else:
        for i in range(b):
            arr3.append(arr2.pop())

for i in arr3[::-1]:
    print(i)
