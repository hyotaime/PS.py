import sys

input = sys.stdin.readline
a = input().strip()
b = input().strip()

rst = []
for i in range(len(a)):
    rst.append(max(int(a[i]), int(b[i])))
for i in rst:
    print(i, end='')
