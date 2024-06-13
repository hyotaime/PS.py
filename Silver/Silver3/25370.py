from itertools import combinations_with_replacement

n = int(input())
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rst = set()
for i in range(1, n + 1):
    for p in combinations_with_replacement(c, i):
        s = 1
        for j in p:
            s *= j
        rst.add(s)
print(len(rst))
