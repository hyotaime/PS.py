import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x):
    global cnt
    visited[x] = cnt
    link[x].sort()
    for l in link[x]:
        if visited[l] == 0:
            cnt += 1
            dfs(l)


n, m, r = map(int, input().split())
link = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
dfs(r)
for i in range(1, n + 1):
    print(visited[i])
