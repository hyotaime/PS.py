import sys

input = sys.stdin.readline
n = input().strip()
con = False
div = False
if '7' in n:
    con = True
if int(n) % 7 == 0:
    div = True
if con and div:
    print("3")
elif con:
    print("2")
elif div:
    print("1")
else:
    print("0")
