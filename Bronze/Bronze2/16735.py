n = int(input())
arr = []
for _ in range(n):
    h, m = map(int, input().split(":"))
    if (h == 6 and m >= 30) or (7 <= h < 19) or (h == 19 and m == 0):
        arr.append((h, m))

arr.sort()
if not arr:
    print(0)
    exit()
sh, sm = arr[0]
eh, em = arr[-1]
if (sh == 6 and sm >= 30) or (7 <= sh < 10) or (sh == 10 and sm == 0):
    if (eh == 6 and em >= 30) or (7 <= eh < 16) or (eh == 16 and em == 0):
        print(24000)
        exit()
    elif (eh == 16 and em > 0) or (16 < eh < 19) or (eh == 19 and em == 0):
        print(36000)
        exit()
if (sh == 10 and sm > 0) or (10 < sh < 15) or (sh == 16 and sm == 0):
    if (eh == 10 and em > 0) or (10 < eh < 15) or (eh == 16 and em == 0):
        print(16800)
        exit()
if (sh == 10 and sm > 0) or (10 < sh < 19) or (sh == 19 and sm == 0):
    if (eh == 16 and em > 0) or (16 < eh < 19) or (eh == 19 and em == 0):
        print(24000)
        exit()
print(0)
