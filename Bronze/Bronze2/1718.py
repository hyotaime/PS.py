s = input()
k = input()
for i in range(len(s)):
    if s[i] == " ":
        print(" ", end="")
    else:
        if ord("a") <= ord(s[i]) - (ord(k[i % len(k)]) - ord("a")) - 1 <= ord("z"):
            print(chr(ord(s[i]) - (ord(k[i % len(k)]) - ord("a")) - 1), end="")
        else:
            print(chr((ord(s[i]) - ord(k[i % len(k)]) - 1) % 27 + ord("a") - 1), end="")
