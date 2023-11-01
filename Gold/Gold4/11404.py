import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
D = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    D[a - 1][b - 1] = min(D[a - 1][b - 1], c)
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if j == k or j == i:
                continue
            D[i][j] = min(D[i][k] + D[k][j], D[i][j])
for d in D:
    for i in d:
        print(i if i != float("inf") else 0, end=" ")
    print()
