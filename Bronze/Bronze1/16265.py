t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    while n > 26:
        arr.append((n - 1) % 26)
        n = (n - 1) // 26
    arr.append(n - 1)
    for i in arr[::-1]:
        print(chr(i + ord('A')), end='')
    print()
