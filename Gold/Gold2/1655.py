import sys
import heapq

input = sys.stdin.readline
n = int(input())
large = []
small = []
mid = int(input())
print(mid)
for _ in range(n-1):
    x = int(input())
    if x > mid:
        heapq.heappush(large, x)
        if len(small) + 1 < len(large):
            heapq.heappush(small, -mid)
            mid = heapq.heappop(large)
    else:
        heapq.heappush(small, -x)
        if len(small) > len(large):
            heapq.heappush(large, mid)
            mid = -heapq.heappop(small)
    print(mid)
