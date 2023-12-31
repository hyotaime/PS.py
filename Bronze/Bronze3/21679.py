import sys

input = sys.stdin.readline
n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
for i in p:
    c[i-1] -= 1
for i in c:
    print("yes" if i < 0 else "no")
