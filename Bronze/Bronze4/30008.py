import sys

input = sys.stdin.readline
n, k = map(int, input().split())
g = list(map(int, input().split()))
gr = []
for i in g:
    p = (i * 100) // n
    if 0 <= p <= 4:
        gr.append(1)
    elif 4 < p <= 11:
        gr.append(2)
    elif 11 < p <= 23:
        gr.append(3)
    elif 23 < p <= 40:
        gr.append(4)
    elif 40 < p <= 60:
        gr.append(5)
    elif 60 < p <= 77:
        gr.append(6)
    elif 77 < p <= 89:
        gr.append(7)
    elif 89 < p <= 96:
        gr.append(8)
    elif 96 < p <= 100:
        gr.append(9)
for i in range(k):
    print(gr[i], end=' ')
