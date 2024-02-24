import sys

input = sys.stdin.readline
n, m, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append([b, c])
btime = [float('INF')] * (n + 1)
btime[x] = 0
queue = []
queue.append([0, x])
while queue:
    t, now = queue.pop(0)
    if btime[now] < t:
        continue
    for i in roads[now]:
        cost = t + i[1]
        if cost < btime[i[0]]:
            btime[i[0]] = cost
            queue.append([cost, i[0]])
rst = 0
for h in range(1, n + 1):
    time = [float('INF')] * (n + 1)
    time[h] = 0
    queue = []
    queue.append([0, h])
    while queue:
        t, now = queue.pop(0)
        if time[now] < t:
            continue
        for i in roads[now]:
            cost = t + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                queue.append([cost, i[0]])
    rst = max(rst, btime[h] + time[x])
print(rst)
