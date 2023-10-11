import sys

input = sys.stdin.readline
n = int(input())
coin = []
for _ in range(n):
    coin = list(map(int, input().split()))
    temp = coin[1]
    chk = True
    for i in coin[2:]:
        if temp * 2 > i:
            chk = False
            break
        else:
            temp = i
    print("Denominations: ", end="")
    for i in coin[1:]:
        print(i, end=" ")
    print()
    if chk:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
