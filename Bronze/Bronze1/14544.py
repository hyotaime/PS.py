import sys

input = sys.stdin.readline
p = int(input())
for i in range(p):
    candidates = {}
    n, m = map(int, input().split())
    for _ in range(n):
        candidate = input().rstrip()
        candidates[candidate] = 0
    for _ in range(m):
        x, r, c = input().split()
        r = int(r)
        candidates[x] += r
    if sorted(candidates.values())[-1] == sorted(candidates.values())[-2]:
        print(f"VOTE {i+1}: THERE IS A DILEMMA")
    else:
        print(f"VOTE {i+1}: THE WINNER IS {max(candidates, key=candidates.get)} {max(candidates.values())}")

