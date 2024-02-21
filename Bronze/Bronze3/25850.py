import sys

input = sys.stdin.readline
p = int(input())
arr = []
for i in range(p):
    c = list(map(int, input().split()))[1:]
    for j in c:
        arr.append((j, i))
arr.sort()
for i in range(len(arr)):
    print(chr(arr[i][1] + 65), end='')
