a = input()
b = input()
c = ""
idx = 0
for i in a:
    if not i.isdigit():
        c += i

print(1 if b in c else 0)