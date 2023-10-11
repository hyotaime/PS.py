import sys

input = sys.stdin.readline
arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

t = int(input())
for i in range(10, 100):
    arr.append(arr[i-1] + arr[i-5])

for _ in range(t):
    n = int(input())
    print(arr[n-1])
