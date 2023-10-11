N = int(input())
P = int(input())
if N >= 20:
    rst = min(P*0.75, P-2000)
elif N >= 15:
    rst = min(P*0.9, P-2000)
elif N >= 10:
    rst = min(P*0.9, P-500)
elif N >= 5:
    rst = P - 500
else:
    rst = P
if rst < 0:
    rst = 0
print(int(rst))
