n = int(input())
s = input()
if n <= 25:
    print(s)
elif '.' not in s[11:-12]:
    print(f"{s[:11]}...{s[-11:]}")
else:
    print(f"{s[:9]}......{s[-10:]}")

