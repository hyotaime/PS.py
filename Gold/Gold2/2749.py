import sys

input = sys.stdin.readline
n = int(input())
def fib_tail(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib_tail(n - 1, b, a + b)

print(fib_tail(n, 0, 1))
