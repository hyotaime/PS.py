import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
arr = [True, False, False]
cnt = 0
for c in s:
    match c:
        case 'L':
            if arr[1]:
                arr[0] = True
                arr[1] = False
            elif arr[2]:
                arr[1] = True
                arr[2] = False
        case 'R':
            if arr[1]:
                arr[2] = True
                arr[1] = False
            elif arr[0]:
                arr[1] = True
                arr[0] = False
    if arr[2]:
        cnt += 1
print(cnt)
