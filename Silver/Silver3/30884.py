import sys

input = sys.stdin.readline
print = sys.stdout.write
s = input().rstrip()
print(s[0])
for i in range(1, len(s)):
    if s[i - 1] == "(" and s[i] == ")":
        print('1')
    elif s[i - 1] == ")" and s[i] == "(":
        print('+')
    print(s[i])
