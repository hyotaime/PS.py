import sys

input = sys.stdin.readline
n = int(input())
names1 = list(map(str, input().split()))
names2 = list(map(str, input().split()))
d = {}
for i in range(n):
    d[names1[i]] = names2[i]
for i in range(n):
    if d[names2[i]] != names1[i] or names1[i] == names2[i]:
        print("bad")
        exit()
print("good")
