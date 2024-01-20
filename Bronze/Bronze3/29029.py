import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
arr = [0, 0, 0, 0]
for d in s:
    match d:
        case 'N':
            arr[0] += 1
        case 'S':
            arr[1] += 1
        case 'E':
            arr[2] += 1
        case 'W':
            arr[3] += 1
arr.sort()
print(sum(arr[:-1]))
