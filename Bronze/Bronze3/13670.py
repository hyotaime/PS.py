import sys

input = sys.stdin.readline
while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    if h2 > h1:
        print((h2 - h1) * 60 + (m2 - m1))
    elif h2 == h1:
        if m2 >= m1:
            print(m2 - m1)
        else:
            print(24 * 60 + (m2 - m1))
    else:
        print((24 + h2 - h1) * 60 + (m2 - m1))
