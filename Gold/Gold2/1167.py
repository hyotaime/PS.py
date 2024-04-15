n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n):
    arr = list(map(int, input().split()))
    node = arr[0]
    for i in range(1, len(arr) - 1, 2):
        tree[node - 1].append((arr[i], arr[i + 1]))

max_node = 0
stack = [(0, 0)]
visited = [False] * n
visited[0] = True
tmp = 0
while stack:
    node, dist = stack.pop()
    if tmp < dist:
        max_node = node
        tmp = dist
    for next_node, next_dist in tree[node]:
        if not visited[next_node - 1]:
            visited[next_node - 1] = True
            stack.append((next_node - 1, dist + next_dist))


stack = [(max_node, 0)]
visited = [False] * n
visited[max_node] = True
rst = 0

while stack:
    node, dist = stack.pop()
    rst = max(rst, dist)
    for next_node, next_dist in tree[node]:
        if not visited[next_node - 1]:
            visited[next_node - 1] = True
            stack.append((next_node - 1, dist + next_dist))

print(rst)
