import math
n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())
print(math.ceil(((m / x) + ((n - m) / y)) / 60 - t) if ((m / x) + ((n - m) / y)) / 60 > t else 0)