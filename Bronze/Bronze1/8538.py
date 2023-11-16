import sys

input = sys.stdin.readline
j = int(input())
names = []
for _ in range(j):
    name = input().rstrip()
    name = name.replace("-", "").upper()
    if name not in names:
        names.append(name)
print(len(names))
