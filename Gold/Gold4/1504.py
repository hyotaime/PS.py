import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
k = 1
link = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    link[a].append([b, c])
    link[b].append([a, c])
distance = [float('INF')] * (n + 1)
distance[k] = 0
queue = []
heapq.heappush(queue, [0, k])
while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for i in link[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, [cost, i[0]])
u, v = map(int, input().split())
k = u
distance2 = [float('INF')] * (n + 1)
distance2[k] = 0
queue = []
heapq.heappush(queue, [0, k])
while queue:
    dist, now = heapq.heappop(queue)
    if distance2[now] < dist:
        continue
    for i in link[now]:
        cost = dist + i[1]
        if cost < distance2[i[0]]:
            distance2[i[0]] = cost
            heapq.heappush(queue, [cost, i[0]])
k = v
distance3 = [float('INF')] * (n + 1)
distance3[k] = 0
queue = []
heapq.heappush(queue, [0, k])
while queue:
    dist, now = heapq.heappop(queue)
    if distance3[now] < dist:
        continue
    for i in link[now]:
        cost = dist + i[1]
        if cost < distance3[i[0]]:
            distance3[i[0]] = cost
            heapq.heappush(queue, [cost, i[0]])
rst = min(distance[v] + distance2[n] + distance3[u], distance[u] + distance3[n] + distance3[u])
if rst == float('INF'):
    print(-1)
else:
    print(rst)
