t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    rst = n
    visited = [False] * (n + 1)

    for i in range(n):
        if arr[i] == i + 1:
            visited[i + 1] = True
            rst -= 1

    for i in range(n):
        if visited[i + 1]:
            continue
        visited[i + 1] = True
        stack = [i + 1]
        team = [i + 1]

        while stack:
            x = stack.pop()
            nx = arr[x - 1]
            if not visited[nx]:
                visited[nx] = True
                stack.append(nx)
                team.append(nx)
            else:
                # 이미 방문처리가 완료된 노드가 team에 존재하면 그 노드부터 끝까지는 순환한다.
                if nx in team:
                    rst -= len(team[team.index(nx):])

    print(rst)
