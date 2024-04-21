t = int(input())
for _ in range(t):
    a, b = map(str, input().split())
    a = float(a)
    match b:
        case "kg":
            print(f"{a * 2.2046:.4f} lb")
        case "lb":
            print(f"{a * 0.4536:.4f} kg")
        case "l":
            print(f"{a * 0.2642:.4f} g")
        case "g":
            print(f"{a * 3.7854:.4f} l")

