t = int(input())
for _ in range(t):
    n = int(input())
    print("1" if n & -n == n else "0")
