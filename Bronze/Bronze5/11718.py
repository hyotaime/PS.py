while True:
    try:
        print(input().rstrip())
    except EOFError:
        break
