t = int(input())
for _ in range(t):
    d = {}
    arr = input().split()
    for a in arr:
        b = a[0]
        if b in d:
            d[b] += 1
        else:
            d[b] = 1

    print(max(d.values()))