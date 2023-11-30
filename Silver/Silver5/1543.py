import sys

input = sys.stdin.readline
doc = input().rstrip()
word = input().rstrip()
cnt = 0
i = 0
while True:
    if len(doc[i:]) < len(word):
        break
    if doc[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1
print(cnt)
