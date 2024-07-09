n = int(input())
d = {}
for _ in range(n):
    a = input()
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
if max(d.values()) > n - max(d.values()):
    print(max(d, key=d.get))
else:
    print('NONE')
