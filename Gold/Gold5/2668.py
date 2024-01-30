import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    a = int(input())
    graph[i].append(a)

rst = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    stack = [i]
    arr1, arr2 = set(), set()
    while stack:
        x = stack.pop()
        if not visited[x]:
            visited[x] = True
            for nx in graph[x]:
                stack.append(nx)
                arr1.add(nx)
                arr2.add(x)
    if arr1 == arr2:
        rst.append(i)
print(len(rst))
for r in rst:
    print(r)
