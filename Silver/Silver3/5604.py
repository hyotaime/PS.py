import sys

input = sys.stdin.readline
n = int(input())
stack = [n]


def rec(x):
    if x > 0:
        for i in range(x, 0, -1):
            if i <= stack[-1]:
                stack.append(i)
                rec(x - i)
                stack.pop()
    else:
        if stack:
            print(*stack[1:])


rec(n)
