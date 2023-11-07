import sys

input = sys.stdin.readline
str = input().rstrip()
bomb = input().rstrip()
stack = []
bomb_len = len(bomb)
stack_len = 0
for i in range(len(str)):
    stack.append(str[i])
    stack_len += 1
    if stack_len >= bomb_len:
        if ''.join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()
                stack_len -= 1
print("".join(stack) if stack else "FRULA")
