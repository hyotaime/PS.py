import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)


def dfs(x):
    visited[x] = 1
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
            visited[x] += visited[nx]


dfs(r)

for _ in range(q):
    u = int(input())
    print(visited[u])
