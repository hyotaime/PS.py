from datetime import datetime

a = input()
b = input()
a_time = datetime.strptime(a, '%H:%M:%S')
b_time = datetime.strptime(b, '%H:%M:%S')
delta = (b_time - a_time).total_seconds()
if delta < 0:
    delta += 86400
print(f"{int(delta // 3600):02d}:{int((delta % 3600) // 60):02d}:{int(delta % 60):02d}")

