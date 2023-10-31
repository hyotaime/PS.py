import sys

input = sys.stdin.readline
n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
rst = 0
for i in range(n):
    if list1[i] == list2[i]:
        rst += 1
    elif list1[i] > list2[i]:
        rst += 3
print(rst)
