import sys

input = sys.stdin.readline
while True:
    try:
        n = int(input())
        d = {}
        cnt = 0
        for _ in range(n):
            a, b = input().split()
            if a not in d:
                d[a] = [0, 0]
                if b == 'D':
                    d[a][0] += 1
                else:
                    d[a][1] += 1
            else:
                if b == 'D':
                    d[a][0] += 1
                else:
                    d[a][1] += 1
        for i in d:
            cnt += min(d[i][0], d[i][1])
        print(cnt)
    except:
        break
