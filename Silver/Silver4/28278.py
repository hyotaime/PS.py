import sys

input = sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    op = input().strip()
    if op[0] == '1':
        x = int(op[2:])
        stack.append(x)
    else:
        match int(op[0]):
            case 2:
                if stack:
                    print(stack.pop())
                else:
                    print(-1)
            case 3:
                print(len(stack))
            case 4:
                if stack:
                    print(0)
                else:
                    print(1)
            case 5:
                if stack:
                    print(stack[-1])
                else:
                    print(-1)
