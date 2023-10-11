t = int(input())
for _ in range(t):
    g, c, e = map(int, input().split())
    if e-c < 0:
        print(0)
    elif g == 1:
        print((e-c)*1)
    elif g == 2:
        print((e-c)*3)
    elif g == 3:
        print((e-c)*5)
