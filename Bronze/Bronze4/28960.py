import sys

input = sys.stdin.readline
h, l, a, b = map(int, input().split())
print("YES" if (h >= a/2 and l >= b) or (h >= b/2 and l >= a) else "NO")
