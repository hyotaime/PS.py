import sys

input = sys.stdin.readline
n = int(input())
u = []
for _ in range(n):
    u.append(input().rstrip())
m = int(input())
chk = True
for _ in range(m):
    pw = input().rstrip()
    if pw in u:
        if chk:
            print("Opened by", pw)
            chk = False
        else:
            print("Closed by", pw)
            chk = True
    else:
        print("Unknown", pw)
