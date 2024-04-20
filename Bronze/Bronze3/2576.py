odds = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        odds.append(n)
odds.sort()
if odds:
    print(sum(odds))
    print(odds[0])
else:
    print(-1)
