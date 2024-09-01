a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())
p -= 1
m -= 1
n -= 1
if p % (a + b) < a and p % (c + d) < c:
    print(2)
elif p % (a + b) < a or p % (c + d) < c:
    print(1)
else:
    print(0)
if m % (a + b) < a and m % (c + d) < c:
    print(2)
elif m % (a + b) < a or m % (c + d) < c:
    print(1)
else:
    print(0)
if n % (a + b) < a and n % (c + d) < c:
    print(2)
elif n % (a + b) < a or n % (c + d) < c:
    print(1)
else:
    print(0)
