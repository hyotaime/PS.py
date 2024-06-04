t = int(input())
for _ in range(t):
    n = int(input())
    total_c, gpa = 0, 0
    for _ in range(n):
        c, g = map(float, input().split())
        total_c += c
        gpa += c * g
    print(int(total_c), round(gpa / total_c, 1))
