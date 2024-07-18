n = int(input())
x, y = map(float, input().split())
for _ in range(n - 1):
    dir, d = input().split()
    d = int(d)
    match dir:
        case 'N':
            y += d
        case 'S':
            y -= d
        case 'E':
            x += d
        case 'W':
            x -= d
        case 'NE':
            x += d / (2 ** 0.5)
            y += d / (2 ** 0.5)
        case 'SE':
            x += d / (2 ** 0.5)
            y -= d / (2 ** 0.5)
        case 'SW':
            x -= d / (2 ** 0.5)
            y -= d / (2 ** 0.5)
        case 'NW':
            x -= d / (2 ** 0.5)
            y += d / (2 ** 0.5)
print(f'{x:.6f} {y:.6f}')
