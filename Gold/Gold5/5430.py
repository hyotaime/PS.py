import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = []
    if n == 0:
        input()
    elif n == 1:
        arr = [int(input().rstrip()[1:-1])]
    elif n > 1:
        arr = list(map(int, input().rstrip()[1:-1].split(',')))

    rev = 0

    for f in p:
        if f == 'R':
            rev += 1
        elif f == 'D':
            if not arr:
                print('error')
                break
            else:
                if rev % 2 == 0:
                    arr.pop(0)
                else:
                    arr.pop()
    else:
        print('[', end='')
        if rev % 2 == 1:
            arr.reverse()
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i], end='')
            else:
                print(arr[i], end=',')
        print(']')
