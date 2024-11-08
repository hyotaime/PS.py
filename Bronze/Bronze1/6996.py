t = int(input())
for _ in range(t):
    a, b = input().split()
    for i in range(26):
        c = chr(i + ord('a'))
        if a.count(c) != b.count(c):
            print(f"{a} & {b} are NOT anagrams.")
            break
    else:
        print(f"{a} & {b} are anagrams.")
