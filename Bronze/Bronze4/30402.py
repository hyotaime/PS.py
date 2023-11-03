import sys

input = sys.stdin.readline
p = [list(map(str, input().split())) for _ in range(15)]
for i in range(15):
    if 'w' in p[i]:
        print("chunbae")
        break
    elif 'b' in p[i]:
        print("nabi")
        break
    elif 'g' in p[i]:
        print("yeongcheol")
        break
