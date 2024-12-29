t = int(input())
for _ in range(t):
    n = int(input())
    if n > 180:
        n -= 180
    if n < 5 or n >= 175:
        print(18)
    elif n < 95:
        print(f"0{int(n / 10 + 0.5)}")
    else:
        print(int(n / 10 + 0.5))
