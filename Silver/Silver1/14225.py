import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
rst = 0
for i in num_list:
    # 1을 더했을 때 그 다음 수보다 작다면 그 수는 만들 수 없는 수이다
    if rst + 1 < i:
        break
    rst += i
print(rst + 1)
