import sys

input = sys.stdin.readline
w = 1
while True:
    n = int(input())
    visit = {}
    if n == 0:
        break
    for _ in range(n):
        s = input().rstrip()
        if s in visit:
            visit[s] += 1
        else:
            visit[s] = 1
    print("Week", w, len(visit))
    w += 1
