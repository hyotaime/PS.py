h, m = map(int, input().split(':'))
n = int(input())
while True:
    if m == 0:
        n -= h
        if n <= 0:
            break
        m = 15
    elif m < 15:
        m = 15
    elif m == 15:
        n -= 1
        if n <= 0:
            break
        m = 30
    elif m < 30:
        m = 30
    elif m == 30:
        n -= 1
        if n <= 0:
            break
        m = 45
    elif m < 45:
        m = 45
    elif m == 45:
        n -= 1
        if n <= 0:
            break
        m = 0
        h += 1
        if h > 12:
            h = 1
    else:
        m = 0
        h += 1
        if h > 12:
            h = 1

print(f"{h:02d}:{m:02d}")
