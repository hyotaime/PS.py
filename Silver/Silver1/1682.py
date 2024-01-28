import sys
from collections import deque

input = sys.stdin.readline
arr = tuple(map(int, input().split()))
origin = (1, 2, 3, 4, 5, 6, 7, 8)

queue = deque([(origin, 0)])
chk = set()

while queue:
    tmp, cnt = queue.popleft()
    if tmp == arr:
        print(cnt)
        break

    tmp2 = (tmp[7], tmp[6], tmp[5], tmp[4], tmp[3], tmp[2], tmp[1], tmp[0])
    if tmp2 not in chk:
        chk.add(tmp2)
        queue.append((tmp2, cnt + 1))

    tmp2 = (tmp[3], tmp[0], tmp[1], tmp[2], tmp[5], tmp[6], tmp[7], tmp[4])
    if tmp2 not in chk:
        chk.add(tmp2)
        queue.append((tmp2, cnt + 1))

    tmp2 = (tmp[0], tmp[2], tmp[5], tmp[3], tmp[4], tmp[6], tmp[1], tmp[7])
    if tmp2 not in chk:
        chk.add(tmp2)
        queue.append((tmp2, cnt + 1))

    tmp2 = (tmp[4], tmp[1], tmp[2], tmp[3], tmp[0], tmp[5], tmp[6], tmp[7])
    if tmp2 not in chk:
        chk.add(tmp2)
        queue.append((tmp2, cnt + 1))
