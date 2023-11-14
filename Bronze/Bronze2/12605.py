import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = input().split()
    print(f"Case #{i+1}:", *s[::-1])
