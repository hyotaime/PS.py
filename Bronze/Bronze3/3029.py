import datetime


a = datetime.datetime.strptime(input(), "%H:%M:%S")
b = datetime.datetime.strptime(input(), "%H:%M:%S")
if a == b:
    print("24:00:00")
else:
    print(datetime.datetime.strptime(str(b - a).split()[-1], "%H:%M:%S").strftime("%H:%M:%S"))
