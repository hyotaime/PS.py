t = int(input())
for i in range(t):
    s = input()
    print(f'String #{i}')
    for c in s:
        if c == 'Z':
            print('A', end='')
        else:
            print(chr(ord(c) + 1), end='')
    print()
    print()
