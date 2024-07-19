n = int(input())
s = input().split()
cnt = 0
for j in s:
    if j[0].isupper():
        for k in j[1:]:
            if k in '.!?':
                continue
            if not k.islower():
                break
        else:
            cnt += 1
    if j[-1] in '.!?':
        print(cnt)
        cnt = 0
