a = input()
b = input()
arr = [0] * 26
for i in range(26):
    c = chr(i + ord("a"))
    arr[i] = max(a.count(c), b.count(c))

for i in range(26):
    c = chr(i + ord("a"))
    print(c * arr[i], end="")
