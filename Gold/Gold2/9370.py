import sys
import heapq

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    roads = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads[a].append([b, d])
        roads[b].append([a, d])
    dest = []
    for _ in range(t):
        dest.append(int(input()))
    dest.sort()
    s_time = [float('INF')] * (n + 1)
    s_time[s] = 0
    queue = []
    heapq.heappush(queue, [0, s])
    while queue:
        t, now = heapq.heappop(queue)
        if s_time[now] < t:
            continue
        for i in roads[now]:
            cost = t + i[1]
            if cost < s_time[i[0]]:
                s_time[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])
    g_time = [float('INF')] * (n + 1)
    g_time[g] = 0
    queue = []
    heapq.heappush(queue, [0, g])
    while queue:
        t, now = heapq.heappop(queue)
        if g_time[now] < t:
            continue
        for i in roads[now]:
            cost = t + i[1]
            if cost < g_time[i[0]]:
                g_time[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])
    h_time = [float('INF')] * (n + 1)
    h_time[h] = 0
    queue = []
    heapq.heappush(queue, [0, h])
    while queue:
        t, now = heapq.heappop(queue)
        if h_time[now] < t:
            continue
        for i in roads[now]:
            cost = t + i[1]
            if cost < h_time[i[0]]:
                h_time[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])
    rst = []
    for i in dest:
        # float('INF')는 어떤값을 더해도 float('INF')이므로 더해도 상관없다. s_time[i]가 float('INF')인 경우를 제외해야 한다.
        if (s_time[i] == s_time[g] + g_time[h] + h_time[i] or s_time[i] == s_time[h] + h_time[g] + g_time[i]) and s_time[i] != float('INF'):
            rst.append(i)
    rst.sort()
    print(*rst)
