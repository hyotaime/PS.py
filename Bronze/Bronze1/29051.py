import sys

input = sys.stdin.readline
d = {'A': 2, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 2, 'G': 1, 'H': 3, 'I': 3, 'J': 2, 'K': 3, 'L': 1, 'M': 1, 'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
s = input().rstrip()
rst = 0
for c in s:
    rst += d[c]
print(rst)
