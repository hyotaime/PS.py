import re
s = input()
q = re.findall(r'(What is[^\.]*\?)', s)
for a in q:
    arr = a.split("?")[:-1]
    for rst in arr:
        print(f'{rst.strip().replace("What is", "Forty-two is")}.')