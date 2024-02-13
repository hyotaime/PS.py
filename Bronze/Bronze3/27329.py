import sys

input = sys.stdin.readline
n = int(input())
s = input().strip()
print('Yes' if s[:n//2] == s[n//2:] else 'No')
