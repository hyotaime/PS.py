import sys

input = sys.stdin.readline
set_chars = set()
n = int(input())
chars = input().split()
for _ in range(n):
    set_chars.update(chars[_])

m = int(input())
num = input().split()
for _ in range(m):
    set_chars.update(num[_])

k = int(input())
chs = input().split()
for ch in chs:
    if ch in set_chars:
        set_chars.remove(ch)

input()
lines = input()

chk = False
rst = []
for line in lines:
    for c in line:
        if c in set_chars or c == ' ':
            if chk:
                rst.append("\n")
                chk = False
            continue
        rst.append(c)
        chk = True

print("".join(rst), end="")
