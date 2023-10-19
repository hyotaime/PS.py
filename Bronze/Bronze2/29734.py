import sys

input = sys.stdin.readline
N, M = map(int, input().split())
T, S = map(int, input().split())
time_at_home = N + ((N - 1) // 8) * S
time_at_library = M + ((M - 1) // 8) * S + ((M - 1) // 8) * 2*T + T
print("Zip" if time_at_home < time_at_library else "Dok")
print(min(time_at_home, time_at_library))
