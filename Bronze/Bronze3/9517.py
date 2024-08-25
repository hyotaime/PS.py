k = int(input())
n = int(input())
a, b = k - 1, 0
for _ in range(n):
    t, z = input().split()
    t = int(t)
    if b + t > 210:
        break
    if z == "T":
        a += 1
    b += t

print(a % 8 + 1)
