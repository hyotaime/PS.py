import sys

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    visited = [0] * (V + 1)
    for i in range(1, V + 1):
        if visited[i] == 0:
            visited[i] = 1
            stack = [i]
            while stack:
                x = stack.pop()
                for nx in graph[x]:
                    if visited[nx] == 0:
                        visited[nx] = -visited[x]
                        stack.append(nx)
                    elif visited[x] == visited[nx]:
                        is_bipartite = False
                        break

    print('YES' if is_bipartite else 'NO')
