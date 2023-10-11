import sys

input = sys.stdin.readline
n = int(input())
file = []
for _ in range(n):
    file.append(input().strip())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a - 1, b):
        print(file[i])
