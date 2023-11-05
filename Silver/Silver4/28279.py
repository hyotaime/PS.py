import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deque = deque()
for _ in range(n):
    op = input().strip()
    if op.split()[0] == '1':
        x = int(op.split()[1])
        deque.appendleft(x)
    elif op.split()[0] == '2':
        x = int(op.split()[1])
        deque.append(x)
    else:
        match op:
            case '3':
                if deque:
                    print(deque.popleft())
                else:
                    print(-1)
            case '4':
                if deque:
                    print(deque.pop())
                else:
                    print(-1)
            case '5':
                print(len(deque))
            case '6':
                if deque:
                    print(0)
                else:
                    print(1)
            case '7':
                if deque:
                    print(deque[0])
                else:
                    print(-1)
            case '8':
                if deque:
                    print(deque[-1])
                else:
                    print(-1)
