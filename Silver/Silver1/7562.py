import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    n_x, n_y = map(int, input().split())
    m_x, m_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    visited[n_x][n_y] = 1
    dq = deque([(n_x, n_y)])
    while dq:
        x, y = dq.popleft()
        if x == m_x and y == m_y:
            break
        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dq.append((nx, ny))
    print(visited[m_x][m_y] - 1)
