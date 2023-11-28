import sys

input = sys.stdin.readline
i = 1
while True:
    n = int(input())
    if n == 0:
        break
    names = [[input().rstrip(), 1] for _ in range(n)]
    for _ in range(2*n-1):
        a, b = input().rstrip().split()
        a = int(a)-1
        if names[a][1]:
            names[a][1] = 0
        else:
            names[a][1] = 1
    for name in names:
        if name[1] == 0:
            print(i, name[0])
            break
    i += 1
