import sys

input = sys.stdin.readline
s = input().rstrip()
print('hiss' if 'ss' in s else 'no hiss')
