import sys

input = sys.stdin.readline
word = input().rstrip()
rsts = []
for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
         rsts.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
print(sorted(rsts)[0])
