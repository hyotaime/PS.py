i = 1
while True:
    try:
        a, b = input().split()
        if len(a) == 1:
            print(f"Case {i}: UNIQUE")
        elif a[-1] == 'b':
            if a[0] == 'A':
                print(f"Case {i}: G# {b}")
            else:
                print(f"Case {i}: {chr(ord(a[0]) - 1)}# {b}")
        else:
            if a[0] == 'G':
                print(f"Case {i}: Ab {b}")
            else:
                print(f"Case {i}: {chr(ord(a[0]) + 1)}b {b}")
        i += 1
    except:
        break
