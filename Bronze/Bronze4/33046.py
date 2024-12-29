a = sum(list(map(int, input().split())))
a %= 4
b = sum(list(map(int, input().split())))
b = (b + a - 1) % 4
print(b if b != 0 else 4)
