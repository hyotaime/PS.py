import datetime
import sys

input = sys.stdin.readline
h, m, s = map(int, input().split())
print((datetime.datetime(2000, 1, 1, h, m, s) + datetime.timedelta(seconds=1)).strftime("%H:%M:%S"))
