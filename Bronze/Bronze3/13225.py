import sys

input = sys.stdin.readline
c = int(input())


def is_prime(n):
    end = int(n ** (1 / 2))
    for i in range(2, end + 1):
        if n % i == 0:
            return False
    return True


for _ in range(c):
    n = int(input())
    if n == 1:
        print(n, 1)
    elif is_prime(n):
        print(n, 2)
    else:
        rst = 2
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                rst += 1
        print(n, rst)
