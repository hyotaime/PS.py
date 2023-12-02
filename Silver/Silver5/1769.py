import sys

input = sys.stdin.readline
x = input().rstrip()
y = 0
cnt = 0
while len(x) > 1:
    for i in x:
        i = int(i)
        y += i
    cnt += 1
    if y < 10:
        x = y
        break
    else:
        x = str(y)
        y = 0
print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")
