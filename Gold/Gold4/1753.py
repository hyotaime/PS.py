import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
link = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    link[a].append([b, c])
distance = [float('INF')] * (v + 1)
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
for i in range(1, v + 1):
    if distance[i] == float('INF'):
        print('INF')
    else:
        print(distance[i])
