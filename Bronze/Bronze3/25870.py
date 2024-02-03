import sys

input = sys.stdin.readline
s = input().rstrip()
alpha = {}
for c in s:
    if c not in alpha:
        alpha[c] = 0
    alpha[c] += 1
    alpha[c] %= 2

rst = -1
for a in alpha:
    if rst != alpha[a]:
        if rst != -1:
            rst = 2
            break
        rst = alpha[a]
print(rst)
