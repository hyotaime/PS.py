import sys

input = sys.stdin.readline
n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def bfs(start):
    visited = [0] * (n + 1)
    queue = [start]
    visited[start] = 1
    while queue:
        now = queue.pop(0)
        for i in node[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1
    return sum(visited) - (n + 1)


rst = []
for i in range(1, n + 1):
    rst.append(bfs(i))
print(rst.index(min(rst)) + 1)
