import math

n = int(input())
for _ in range(n):
    a, b, c = map(str, input().split())
    if a == 'H':
        print(f"{-math.log10(float(c)):.2f}")
    else:
        print(f"{14 + math.log10(float(c)):.2f}")
