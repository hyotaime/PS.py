n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * n
for i in range(n):
    cnt[i] = arr.count(i + 1)

m = max(cnt)
if cnt.count(m) > 1:
    print("skipped")
else:
    print(cnt.index(m) + 1)