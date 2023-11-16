import sys

input = sys.stdin.readline
while True:
    flight = input().rstrip()
    seats = {}
    codes = {'L': 120, 'S': 150, 'B': 150, 'N': 40, 'C': 160, 'D': 100, 'R': 100, 'O': 100}
    if flight == "#":
        break
    while True:
        tmp = input()
        seat = tmp.split()[0]
        if seat == "00A":
            break
        code = tmp.split()[1]
        if code not in codes:
            continue
        if seat not in seats:
            seats[seat] = codes[code]
        else:
            seats[seat] += codes[code]
    cnt = 0
    for seat in seats:
        if seats[seat] >= 200:
            cnt += 1
    print(flight, cnt)
