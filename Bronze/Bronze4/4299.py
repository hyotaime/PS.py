a, b = map(int, input().split())
if a < b or (a-b) % 2 == 1:
    print(-1)
elif (a-b) % 2 == 0:
    print(f"{int((a-b)/2+b)} {int((a-b)/2)}")
