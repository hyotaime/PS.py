import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
absheap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap or absheap:
            if heap and not absheap:
                print(heapq.heappop(heap))
            elif absheap and not heap:
                print(-heapq.heappop(absheap))
            elif heap and absheap and heap[0] >= absheap[0]:
                print(-heapq.heappop(absheap))
            else:
                print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x) if x > 0 else heapq.heappush(absheap, abs(x))
