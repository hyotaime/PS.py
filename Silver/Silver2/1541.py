import sys

input = sys.stdin.readline
s = input().rstrip()
rst = sum(map(int, s.split('-')[0].split('+')))
for i in s.split('-')[1:]:
    rst -= sum(map(int, i.split('+')))
print(rst)
