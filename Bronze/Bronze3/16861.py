import sys

input = sys.stdin.readline
n = int(input())
while True:
    arr = str(n)
    s = sum(map(int, arr))
    if n % s == 0:
        print(n)
        break
    n += 1
