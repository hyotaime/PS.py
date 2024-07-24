n = 0
op = '+'
while True:
    a = input()
    if a.isdigit():
        a = int(a)
        match op:
            case '+':
                n += a
            case '-':
                n -= a
            case '*':
                n *= a
            case '/':
                n //= a
    else:
        if a == '=':
            print(n)
            exit(0)
        op = a
