import sys
from itertools import combinations

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    if n > 2 ** 5:
        print(0)
    else:
        rst = 2 ** 3 + 1
        comb = combinations(arr, 3)
        for c in comb:
            d = 0
            for i in range(4):
                if c[0][i] != c[1][i]:
                    d += 1
            for i in range(4):
                if c[0][i] != c[2][i]:
                    d += 1
            for i in range(4):
                if c[1][i] != c[2][i]:
                    d += 1
            rst = min(rst, d)
        print(rst)
