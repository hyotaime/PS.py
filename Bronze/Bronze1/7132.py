import sys

input = sys.stdin.readline
m, n = map(int, input().split())
clock = set()
for i in range(m, n+1):
    for j in range(m, n+1):
        clock.add(j/i)
        clock.add(i/j)
print(len(clock))
