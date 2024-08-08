n = float(input())
while True:
    a = float(input())
    if a == 999:
        break
    print(f'{a - n:0.2f}')
    n = a
