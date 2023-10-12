import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().rstrip()
    match s:
        case "Algorithm":
            print("204")
        case "DataAnalysis":
            print("207")
        case "ArtificialIntelligence":
            print("302")
        case "CyberSecurity":
            print("B101")
        case "Network":
            print("303")
        case "Startup":
            print("501")
        case "TestStrategy":
            print("105")
