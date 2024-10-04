arr = list(map(int, input().split()))
s = 0
for i in range(0, 10, 2):
    a = arr[i]
    l = arr[i + 1]
    s += a * l
s //= 5
n, k = map(int, input().split())
print(n * s // k)