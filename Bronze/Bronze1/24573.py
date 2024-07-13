n = int(input())
cnt = 0
for i in range(0, n // 5 + 1):
    if (n - 5 * i) % 4 == 0:
        cnt += 1
print(cnt)
