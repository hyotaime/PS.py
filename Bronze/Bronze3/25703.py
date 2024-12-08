n = int(input())
print("int a;")
print("int *ptr = &a;")
for i in range(1, n):
    print(f"int {'*' * (i + 1)}ptr{i + 1} = &ptr{i if i > 1 else ''};")
