import sys

input = sys.stdin.readline
n = int(input())
a, b = 0, 0
turn = False
while n > 0:
    if n % 2 == 1:
        if turn:
            a += n // 2 + 1
            turn = False
        else:
            b += n // 2 + 1
            turn = True
        n //= 2
    else:
        if turn:
            a += n // 2
            turn = False
        else:
            b += n // 2
            turn = True
        n //= 2
print(a, b)
