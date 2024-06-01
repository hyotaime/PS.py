import sys

input = sys.stdin.readline
print = sys.stdout.write


n = int(input())
for _ in range(n):
    s = input()
    print(s[0].upper() + s[1:])
