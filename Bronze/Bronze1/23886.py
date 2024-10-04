s = input()
a = int(s[1]) - int(s[0])
if a <= 0 or int(s[-1]) - int(s[-2]) >= 0:
    print("NON ALPSOO")
    exit()
for i in range(2, len(s)):
    if int(s[i]) - int(s[i - 1]) == 0:
        print("NON ALPSOO")
        break
    elif a * (int(s[i]) - int(s[i - 1])) < 0:
        a = int(s[i]) - int(s[i - 1])
    elif a != int(s[i]) - int(s[i - 1]):
        print("NON ALPSOO")
        break
else:
    print("ALPSOO")
