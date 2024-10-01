n, p, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rst = []
for i in range(n):
    x, y = a[i], b[i]
    if x == y:
        rst.append(0)
    elif (x - y) * (p - q) < 0:
        if (x - y) % (q - p) == 0 and (x - y) // (q - p) <= 10000:
            rst.append((x - y) // (q - p))
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()

print("YES")
print(*rst)
