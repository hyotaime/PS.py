import sys

input = sys.stdin.readline
l, g, r = map(int, input().split())
lights = [False] * l
dict = {}
for _ in range(g):
    name, a, d = input().split()
    a = int(a)
    d = int(d)
    dict[name] = (a, d)
for _ in range(r):
    name = input().rstrip()
    a, d = dict[name]
    print(name, a, d)
    while a <= l:
        lights[a-1] = True if not lights[a-1] else False
        a += d
    print(lights)
print(lights.count(True))
