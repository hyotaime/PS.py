import sys

input = sys.stdin.readline
l, t = 0, 0
for _ in range(9):
    match input().strip():
        case 'Tiger':
            t += 1
        case 'Lion':
            l += 1
print('Tiger' if t > l else 'Lion')
