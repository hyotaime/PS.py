import sys

input = sys.stdin.readline
n = str(input()).strip()
if len(n) == 4:
    print(20)
elif len(n) == 3:
    if n[1] == '0':
        print(10 + int(n[2]))
    else:
        print(int(n[0]) + 10)
else:
    print(int(n[0]) + int(n[1]))
