import sys

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    rst = False
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    dist = [2147483647] * (n + 1)  # inf를 사용하면 모든 노드의 연결관계를 고려하지 않음. 따라서 int max를 사용함.
    dist[1] = 0
    for i in range(n):
        for j in range(1, n + 1):
            for x, w in graph[j]:
                if dist[x] > dist[j] + w:
                    dist[x] = dist[j] + w
                    if i == n - 1:
                        rst = True
                        break

    print("YES" if rst else "NO")
