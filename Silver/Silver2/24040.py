import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print("TAK" if n % 3 == 2 or n % 9 == 0 else "NIE")
