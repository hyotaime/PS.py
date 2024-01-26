# python3 TLE, pypy3 AC
import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10000
    queue = deque([(a, '')])
    visited[a] = True
    while queue:
        num, op = queue.popleft()
        if num == b:
            print(op)
            break
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, op + 'D'))
        s = num - 1 if num != 0 else 9999
        if not visited[s]:
            visited[s] = True
            queue.append((s, op + 'S'))
        l = (num % 1000) * 10 + num // 1000
        if not visited[l]:
            visited[l] = True
            queue.append((l, op + 'L'))
        r = (num % 10) * 1000 + num // 10
        if not visited[r]:
            visited[r] = True
            queue.append((r, op + 'R'))
