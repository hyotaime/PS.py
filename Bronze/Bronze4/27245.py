import sys

input = sys.stdin.readline
w = int(input())
l = int(input())
n = int(input())
print("good" if min(w, l) / n >= 2 >= max(w, l) / min(w, l) else "bad")
