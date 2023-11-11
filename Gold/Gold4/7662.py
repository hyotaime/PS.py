import sys
import heapq

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    max_q = []
    min_q = []
    k = int(input())
    erased = [False] * k
    for i in range(k):
        op, num = input().rstrip().split()
        num = int(num)
        match op:
            case 'I':
                heapq.heappush(max_q, (-num, i))
                heapq.heappush(min_q, (num, i))
            case 'D':
                if num > 0:
                    if max_q:
                        erased[heapq.heappop(max_q)[1]] = True
                else:
                    if min_q:
                        erased[heapq.heappop(min_q)[1]] = True
                while max_q and erased[max_q[0][1]]:
                    heapq.heappop(max_q)
                while min_q and erased[min_q[0][1]]:
                    heapq.heappop(min_q)

    if max_q and min_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print('EMPTY')
