while True:
    n = int(input())
    if n == 0:
        break
    while n >= 10:
        n = sum(map(int, str(n)))
    print(n)
