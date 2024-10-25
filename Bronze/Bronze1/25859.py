s = input()
arr = []
for i in range(26):
    arr.append((-(s.count(chr(i + ord('a')))), chr(i + ord('a'))))

arr.sort()
for cnt, c in arr:
    print(c * -cnt, end='')
