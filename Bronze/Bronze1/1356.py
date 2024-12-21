n = input()
for i in range(1, len(n)):
    a, b = 1, 1
    for j in range(i):
        a *= int(n[j])
    for j in range(i, len(n)):
        b *= int(n[j])
    if a == b:
        print("YES")
        break
else:
    print("NO")
