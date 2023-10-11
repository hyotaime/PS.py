import sys

input = sys.stdin.readline
n = int(input())
print("WelcomeToSMUPC"[(n - 1) % 14])
