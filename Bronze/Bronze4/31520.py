import sys

input = sys.stdin.readline
s = input().rstrip()
flag = True
for i in range(len(s)):
    if int(s[i]) != i + 1:
        flag = False
        break
print(len(s) if flag else -1)
