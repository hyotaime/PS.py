cnt = 1
while True:
    a, b, c = map(str, input().split())
    if b == '0':
        break
    a = float(a) / 63360
    b = int(b)
    c = float(c) / 3600
    l = a * 3.1415927 * b
    print(f'Trip #{cnt}: {l:.2f} {l / c:.2f}')
    cnt += 1
