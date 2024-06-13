n, m = map(int, input().split())
d = dict()
cnt = 0
for _ in range(m):
    a = int(input())
    cnt += 1
    for i in d:
        d[i] += 1
    d[a] = 0
    print(sum(d.values()) + cnt * (n - len(d)))
