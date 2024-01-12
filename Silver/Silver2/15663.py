import sys
from itertools import permutations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in sorted(set(permutations(arr, m))):
    print(*i)
