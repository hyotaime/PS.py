import sys

input = sys.stdin.readline
while True:
    try:
        target, guess = input().split()
    except:
        break
    b, g, w = 0, 0, 0
    rst = guess
    target = list(target)
    guess = list(guess)
    for i in range(len(guess)):
        if guess[i] in target and guess[i] == target[i]:
            b += 1
            guess[i] = '-'
            target[i] = '-'
    for i in range(len(guess)):
        if guess[i] != '-' and guess[i] in target:
            if i > 0 and guess[i] == target[i - 1]:
                g += 1
                target[i - 1] = '-'
                guess[i] = '-'
            elif i < len(guess) - 1 and guess[i] == target[i + 1]:
                g += 1
                target[i + 1] = '-'
                guess[i] = '-'
    for i in range(len(guess)):
        if guess[i] != '-' and guess[i] in target:
            w += 1
            target[target.index(guess[i])] = '-'
            guess[i] = '-'
    print(f"{rst}: {b} black, {g} grey, {w} white")
