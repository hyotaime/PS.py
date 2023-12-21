import sys

input = sys.stdin.readline
while True:
    l, w, h, v = map(int, input().split())
    if l == w == v == h == 0:
        break
    if v == 0:
        v = l * w * h
    elif l == 0:
        l = v // (w * h)
    elif w == 0:
        w = v // (l * h)
    elif h == 0:
        h = v // (l * w)
    print(l, w, h, v)
