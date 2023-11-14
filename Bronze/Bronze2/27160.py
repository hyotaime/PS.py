import sys

input = sys.stdin.readline
n = int(input())
hali = {}
for _ in range(n):
    f, n = input().split()
    n = int(n)
    if f in hali:
        hali[f] += n
    else:
        hali[f] = n
for _ in range(len(hali)):
    if hali.popitem()[1] == 5:
        print("YES")
        sys.exit()
print("NO")
