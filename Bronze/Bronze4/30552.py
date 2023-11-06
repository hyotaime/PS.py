import sys

input = sys.stdin.readline
n = int(input())
names = []
for _ in range(n):
    name = input().rstrip()
    if name == "Present!":
        names.pop()
    else:
        names.append(name)
if names:
    print("\n".join(names))
else:
    print("No Absences")
