t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())

    # 최소 스패닝 트리의 간선의 수는 n - 1이다.
    print(n - 1)
