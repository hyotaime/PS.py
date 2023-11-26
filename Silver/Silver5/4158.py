import sys

input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    cd1, cd2 = set(), set()
    for _ in range(n):
        cd1.add(int(input()))
    for _ in range(m):
        cd2.add(int(input()))
    print(len(cd1 & cd2))
