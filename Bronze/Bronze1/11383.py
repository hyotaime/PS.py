import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
for i in range(n):
    s = input().rstrip()
    for j in range(m * 2):
        if s[j] != arr[i][j//2]:
            print("Not Eyfa")
            exit()
print("Eyfa")
