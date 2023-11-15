import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    teams = [int(input()) for _ in range(n)]
    for team in teams[::-1]:
        print(team)
    print(0)
