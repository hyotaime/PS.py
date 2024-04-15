for _ in range(3):
    arr = list(map(int, input().split()))
    cnt = arr.count(0)
    match cnt:
        case 0:
            print('E')
        case 1:
            print('A')
        case 2:
            print('B')
        case 3:
            print('C')
        case 4:
            print('D')
