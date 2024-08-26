for a in range(2, 101):
    for b in range(2, 101):
        for c in range(b, 101):
            for d in range(c, 101):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
                elif a ** 3 < b ** 3 + c ** 3 + d ** 3:
                    break
