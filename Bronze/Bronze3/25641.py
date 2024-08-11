n = int(input())
s = input()
a, b = s.count('s'), s.count('t')
for i in range(n):
    if a == b:
        print(s[i:])
        break
    if s[i] == 's':
        a -= 1
    else:
        b -= 1
