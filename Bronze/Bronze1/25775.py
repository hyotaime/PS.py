import sys
from collections import Counter

input = sys.stdin.readline
t = int(input())
words = []
for _ in range(t):
    words.append(input().rstrip())

d = {}
for i in range(max(map(len, words))):
    d[i + 1] = Counter([word[i:i+1] for word in words if len(word) > i]).most_common()

for i in d.keys():
    print(f"{i}:", end=" ")
    print(*sorted(rst[0] for rst in d[i] if rst[1] == d[i][0][1]))
