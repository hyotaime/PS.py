a, b = 0, 0
while True:
    arr = list(input().split())
    match arr[0]:
        case "1":
            if arr[1] == "A":
                a = int(arr[2])
            elif arr[1] == "B":
                b = int(arr[2])
        case "2":
            if arr[1] == "A":
                print(a)
            elif arr[1] == "B":
                print(b)
        case "3":
            x, y = 0, 0
            x = a if arr[1] == "A" else b
            y = a if arr[2] == "A" else b
            if arr[1] == "A":
                a = x + y
            elif arr[1] == "B":
                b = x + y
        case "4":
            x, y = 0, 0
            x = a if arr[1] == "A" else b
            y = a if arr[2] == "A" else b
            if arr[1] == "A":
                a = x * y
            elif arr[1] == "B":
                b = x * y
        case "5":
            x, y = 0, 0
            x = a if arr[1] == "A" else b
            y = a if arr[2] == "A" else b
            if arr[1] == "A":
                a = x - y
            elif arr[1] == "B":
                b = x - y
        case "6":
            x, y = 0, 0
            x = a if arr[1] == "A" else b
            y = a if arr[2] == "A" else b
            if arr[1] == "A":
                a = x // y
            elif arr[1] == "B":
                b = x // y
        case "7":
            break

