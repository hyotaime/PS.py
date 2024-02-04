import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    f = input().rstrip()
    l = input().rstrip()
    print(f'Case {_ + 1}: {l}, {f}')
