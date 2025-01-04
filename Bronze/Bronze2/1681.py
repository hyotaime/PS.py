n, l = input().split()
n = int(n)
i = 0
for _ in range(n):
    i += 1
    while l in str(i):
        i += 1

print(i)
