t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print('#')
        print()
        continue
    print('#' * n)
    for _ in range(n - 2):
        print('#' + 'J' * (n - 2) + '#')
    print('#' * n)
    print()
