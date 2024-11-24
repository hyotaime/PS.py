s = input()
if "A" in s:
    s = s.replace("B", "A").replace("C", "A").replace("D", "A").replace("F", "A")
elif "B" in s:
    s = s.replace("C", "B").replace("D", "B").replace("F", "B")
elif "C" in s:
    s = s.replace("D", "C").replace("F", "C")
else:
    s = "A" * len(s)

print(s)

