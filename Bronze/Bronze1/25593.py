import sys

input = sys.stdin.readline
n = int(input())
work = {}
for _ in range(n):
    etotw = list(map(str, input().split()))
    for name in etotw:
        if name == "-":
            continue
        if name not in work:
            work[name] = 4
        else:
            work[name] += 4
    twtoet = list(map(str, input().split()))
    for name in twtoet:
        if name == "-":
            continue
        if name not in work:
            work[name] = 6
        else:
            work[name] += 6
    ettott = list(map(str, input().split()))
    for name in ettott:
        if name == "-":
            continue
        if name not in work:
            work[name] = 4
        else:
            work[name] += 4
    tttoe = list(map(str, input().split()))
    for name in tttoe:
        if name == "-":
            continue
        if name not in work:
            work[name] = 10
        else:
            work[name] += 10
print("Yes") if not work or max(work.values())-min(work.values()) <= 12 else print("No")
