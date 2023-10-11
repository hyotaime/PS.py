import sys

input = sys.stdin.readline
d, m = map(int, input().split())
day = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
if m == 1:
    print(day[(d - 1) % 7])
elif m == 2:
    print(day[(d - 1 + 31) % 7])
elif m == 3:
    print(day[(d - 1 + 59) % 7])
elif m == 4:
    print(day[(d - 1 + 90) % 7])
elif m == 5:
    print(day[(d - 1 + 120) % 7])
elif m == 6:
    print(day[(d - 1 + 151) % 7])
elif m == 7:
    print(day[(d - 1 + 181) % 7])
elif m == 8:
    print(day[(d - 1 + 212) % 7])
elif m == 9:
    print(day[(d - 1 + 243) % 7])
elif m == 10:
    print(day[(d - 1 + 273) % 7])
elif m == 11:
    print(day[(d - 1 + 304) % 7])
elif m == 12:
    print(day[(d - 1 + 334) % 7])
