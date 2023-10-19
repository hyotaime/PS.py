import sys

input = sys.stdin.readline
n, x = map(float, input().split())
n = int(n)
x = int(round(x*100))
grade = 0
cnt = 0
gr = {"A+": 450, "A0": 400, "B+": 350, "B0": 300, "C+": 250, "C0": 200, "D+": 150, "D0": 100, "F": 0, 450: "A+", 400: "A0", 350: "B+", 300: "B0", 250: "C+", 200: "C0", 150: "D+", 100: "D0", 0: "F"}
for _ in range(int(n)-1):
    c, g = map(str, input().split())
    c = int(c)
    cnt += c
    grade += c * gr[g]
last = int(input())
cnt += last
rst = 0
for _ in range(9):
    tmp = grade + last * rst
    t = tmp // cnt
    if t > x:
        print(gr[rst])
        break
    else:
        if rst == 0:
            rst += 100
        else:
            rst += 50
        if rst == 500:
            print("impossible")
            break
