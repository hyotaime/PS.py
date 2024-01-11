import sys

input = sys.stdin.readline

mod = 1000000007


def ipow(x, p):
    ret, piv = 1, x
    while p:
        if p & 1:
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret


def berlekamp_massey(x):
    ls, cur = [], []
    lf, ld = 0, 0
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + x[i - j - 1] * cur[j]) % mod
        if (t - x[i]) % mod == 0:
            continue
        if not cur:
            cur = [0] * (i + 1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = [0] * (i - lf - 1) + [k]
        for j in ls:
            c.append(-j * k % mod)
        if len(c) < len(cur):
            c.extend([0] * (len(cur) - len(c)))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    return [(i % mod + mod) % mod for i in cur]


def get_nth(rec, dp, n):
    m = len(rec)
    s, t = [0] * m, [0] * m
    s[0] = 1
    if m != 1:
        t[1] = 1
    else:
        t[0] = rec[0]

    def mul(v, w):
        m = len(v)
        t = [0] * (2 * m)
        for j in range(m):
            for k in range(m):
                t[j + k] += v[j] * w[k] % mod
                if t[j + k] >= mod:
                    t[j + k] -= mod
        for j in range(2 * m - 1, m - 1, -1):
            for k in range(1, m + 1):
                t[j - k] += t[j] * rec[k - 1] % mod
                if t[j - k] >= mod:
                    t[j - k] -= mod
        return t[:m]

    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n >>= 1
    ret = 0
    for i in range(m):
        ret += s[i] * dp[i] % mod
    return ret % mod


def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    v = berlekamp_massey(x)
    if not v:
        return 0
    return get_nth(v, x, n)


if __name__ == '__main__':
    k, n = map(int, input().split())
    dp = [[0] * 153 for _ in range(51)]
    for j in range(153):
        dp[0][j] = j
    for i in range(1, k + 1):
        for j in range(153):
            for l in range(1, j + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][l]) % mod

    print(guess_nth_term(dp[k], n))
