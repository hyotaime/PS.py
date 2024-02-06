# Stack을 이용한 DFS는 WA가 나온다. 왜인지는 모르겠다.
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, cnt):
    if cnt == 5:
        print(1)
        exit()
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx, cnt + 1)
            visited[nx] = False


for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, 1)

print(0)
