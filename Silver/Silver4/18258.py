import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deque = deque()
for _ in range(n):
    op = input().strip()
    if op.split()[0] == 'push':
        x = int(op.split()[1])
        deque.append(x)
    else:
        match op:
            case 'pop':
                if deque:
                    print(deque.popleft())
                else:
                    print(-1)
            case 'size':
                print(len(deque))
            case 'empty':
                if deque:
                    print(0)
                else:
                    print(1)
            case 'front':
                if deque:
                    print(deque[0])
                else:
                    print(-1)
            case 'back':
                if deque:
                    print(deque[-1])
                else:
                    print(-1)
