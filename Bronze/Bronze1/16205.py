import re

n, s = input().split()
n = int(n)
match n:
    case 1:
        arr = re.findall(r'[A-Z]?[a-z]+|[A-Z](?![a-z])', s)
    case 2:
        arr = s.split('_')
    case 3:
        arr = re.findall(r'[A-Z][a-z]*|[A-Z]+(?![a-z])', s)

camel = []
snake = []
pascal = []

for i in arr:
    i = i.lower()
    cap = i[0].upper() + i[1:]
    if not camel:
        camel.append(i)
    else:
        camel.append(cap)
    snake.append(i)
    pascal.append(cap)

print("".join(camel))
print("_".join(snake))
print("".join(pascal))
