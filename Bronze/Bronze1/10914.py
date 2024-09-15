n = int(input())
s = list(input().split())
for t in s:
    if len(t) % 2 == 0:
        for i in range(0, len(t), 2):
            print(chr((ord(t[i]) - ord('a') + ord(t[i + 1]) - ord('a') - n) % 26 + ord('a')), end='')
    else:
        for i in range(0, len(t) - 1, 2):
            print(chr((ord(t[i]) - ord('a') + ord(t[i + 1]) - ord('a') - n) % 26 + ord('a')), end='')
    print(' ', end='')
