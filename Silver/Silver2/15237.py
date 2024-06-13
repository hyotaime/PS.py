n, c = map(int, input().split())
arr = list(map(int, input().split()))
d = dict()
for i in arr:
    if i not in d:
        d[i] = 0
    d[i] += 1

for i in sorted(d, key=lambda x: d[x], reverse=True):
    print(f"{i} " * d[i], end="")
