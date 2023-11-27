import sys

input = sys.stdin.readline
month, day, year, time = input().rstrip().split()
cnt = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
cnt += (int(day.replace(',', '')) - 1) * 24 * 60
year = int(year)
match month:
    case 'January':
        month = 1
    case 'February':
        month = 2
    case 'March':
        month = 3
    case 'April':
        month = 4
    case 'May':
        month = 5
    case 'June':
        month = 6
    case 'July':
        month = 7
    case 'August':
        month = 8
    case 'September':
        month = 9
    case 'October':
        month = 10
    case 'November':
        month = 11
    case 'December':
        month = 12
for i in range(1, month):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        cnt += 31 * 24 * 60
    elif i in [4, 6, 9, 11]:
        cnt += 30 * 24 * 60
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            cnt += 29 * 24 * 60
        else:
            cnt += 28 * 24 * 60

total = 31 * 24 * 60 + 31 * 24 * 60 + 30 * 24 * 60 + 31 * 24 * 60 + 30 * 24 * 60 + 31 * 24 * 60 + 31 * 24 * 60 + 30 * 24 * 60 + 31 * 24 * 60 + 30 * 24 * 60 + 31 * 24 * 60
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    total += 29 * 24 * 60
else:
    total += 28 * 24 * 60
print((cnt/total) * 100)
