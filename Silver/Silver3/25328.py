from itertools import combinations

x = input()
y = input()
z = input()
k = int(input())
d = {}
for s in combinations(x, k):
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
for s in combinations(y, k):
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
for s in combinations(z, k):
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

rst = []

for s in sorted(d):
    if d[s] >= 2:
        rst.append("".join(s))

if rst:
    for s in rst:
        print(s)

else:
    print(-1)