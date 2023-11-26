import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    teams = {}
    for _ in range(16):
        team1, team2, score1, score2 = input().split()
        score1, score2 = int(score1), int(score2)
        if score1 > score2:
            if team1 not in teams:
                teams[team1] = 1
            else:
                teams[team1] += 1
        else:
            if team2 not in teams:
                teams[team2] = 1
            else:
                teams[team2] += 1
    print(max(teams, key=teams.get))
