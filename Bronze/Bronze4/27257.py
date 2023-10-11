import sys

input = sys.stdin.readline
s = str(input()).strip()
cnt = 0
chk = False
for n in reversed(s):
    if n == "0" and chk:
        cnt += 1
    elif n != "0" and cnt == 0:
        chk = True
print(cnt)
