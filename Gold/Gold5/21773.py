import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

T, n = map(int, input().split())
heap = []
for _ in range(n):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (-c, a, b))

for _ in range(T):
    c, a, b = heapq.heappop(heap)
    print("%d\n" % a)
    if b > 1:
        heapq.heappush(heap, (c + 1, a, b - 1))
