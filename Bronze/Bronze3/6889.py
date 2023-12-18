import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
adj, noun = [], []
for _ in range(n):
    adj.append(input().rstrip())
for _ in range(m):
    noun.append(input().rstrip())
for a in adj:
    for nn in noun:
        print(a + " as " + nn)
