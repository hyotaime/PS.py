import sys

input = sys.stdin.readline

# https://www.acmicpc.net/blog/view/28
# 피보나치 수를 k로 나눈 나머지는 항상 주기를 가지게 된다.
# 이를 피사노 주기(Pisano Period)라고 한다.
# k = 10^n 일 때, 주기는 15 * 10^(n-1) 이다.
mod = 1000000
p = mod // 10 * 15
fib = [0, 1] + [0] * (p - 2)

n = int(input())

for i in range(2, p):
    fib[i] = (fib[i - 1] + fib[i - 2]) % mod

print(fib[n % p])
