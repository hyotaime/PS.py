import sys

input = sys.stdin.readline
s = input().rstrip()
stack = []
rst = ''
for i in range(len(s)):
    if s[i] not in ['+', '-', '*', '/', '(', ')']:
        rst += s[i]
    else:
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            while stack and stack[-1] != '(':
                rst += stack.pop()
            stack.pop()
        elif s[i] in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                rst += stack.pop()
            stack.append(s[i])
        elif s[i] in ['+', '-']:
            while stack and stack[-1] in ['+', '-', '*', '/']:
                rst += stack.pop()
            stack.append(s[i])
while stack:
    rst += stack.pop()
print(rst)
