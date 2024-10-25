a = input()
b = input()
while len(a) > 1 or len(b) > 1:
    x, y = [], []
    for i in range(len(b)):
        x.append((int(a[i]) + int(b[i])) % 10)

    for i in range(len(a) - 1):
        y.append((int(a[i + 1]) + int(b[i])) % 10)

    a, b = x, y

print(f"{a[0]}{b[0]}")
