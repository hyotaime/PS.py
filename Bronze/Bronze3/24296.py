import sys

input = sys.stdin.readline
n = int(input())
while n % 2 == 1:
    n = n // 2 + 1
print(n)
