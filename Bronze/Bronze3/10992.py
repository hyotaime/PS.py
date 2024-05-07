n = int(input())
for i in range(n - 1):
    print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i else ''))
print('*' * (2 * n - 1))
