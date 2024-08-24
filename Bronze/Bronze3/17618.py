n = int(input())
cnt = 0
for i in range(1, n + 1):
    r = 0
    for c in str(i):
        r += int(c)
    if i % r == 0:
        cnt += 1
print(cnt)
