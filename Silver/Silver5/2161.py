import sys

input = sys.stdin.readline

n = int(input())
cards = [i for i in range(1, n + 1)]
rst = []
while len(cards) > 1:
    rst.append(cards.pop(0))
    cards.append(cards.pop(0))
rst.append(cards.pop(0))
print(*rst)
