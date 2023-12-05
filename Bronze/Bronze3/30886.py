import sys
import math

input = sys.stdin.readline
a = int(input())
r = math.sqrt(a / math.pi)
print(pow(r*2+2, 2))
