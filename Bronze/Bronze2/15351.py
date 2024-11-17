t = int(input())
for _ in range(t):
    s = input().split()
    rst = 0
    for w in s:
        for c in w:
            rst += ord(c) - ord('A') + 1

    if rst == 100:
        print("PERFECT LIFE")
    else:
        print(rst)
