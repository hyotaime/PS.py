t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    dic = {}
    rst = 0
    for _ in range(n):
        s = input()
        a, b, c, d = s.split()[0], s.split()[1], s.split()[2], "".join(s.split()[3:]).lower()
        dic[d] = (int(a), float(b[1:]), float(c[1:]))
    for _ in range(m):
        s = input()
        a, b = s.split()[0], "".join(s.split()[1:]).lower()
        if b in dic:
            rst += min(int(a), dic[b][0]) * (dic[b][1] - dic[b][2])
    print(f"Data Set {i + 1}:")
    print(f"${rst:.2f}")
    print()
