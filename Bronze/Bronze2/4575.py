import sys

input = sys.stdin.readline
while True:
    s = input().rstrip()
    alphabet = [0] * 26
    if s == "END":
        break
    for c in s:
        if c.isalpha():
            alphabet[ord(c)-ord('A')] += 1
    alphabet.sort()
    if alphabet[-1] <= 1:
        print(s)
